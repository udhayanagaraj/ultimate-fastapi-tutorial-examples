from typing import Optional,Any
from pathlib import Path
from fastapi import FastAPI,APIRouter,HTTPException,Query,Request,Depends
from fastapi.templating import Jinja2Templates
from app.schemas import Recipe,ReciepeSearchResults,RecipeCreate
from sqlalchemy.orm import session
from app import deps
from app import crud

ROOT = Path(__file__).resolve().parent.parent
BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))

app = FastAPI(title="Recipe API",openapi_url="/openapi.json")

api_router = APIRouter()

@api_router.get("/",status_code=200)
def root(request:Request,db:session = Depends(deps.get_db)) -> dict:
    recipes = crud.recipe.get_multi(db=db,limit=10)
    return TEMPLATES.TemplateResponse(
        request=request,
        name="index.html",
        context={"recipes":recipes}
    )


@api_router.get("/recipe/{recipe_id}",status_code=200,response_model=Recipe)
def fetch_recipie(*,recipe_id:int,db:session = Depends(deps.get_db)) -> Any:
    result = crud.recipe.get(db=db,id=recipe_id)
    if not result:
        raise HTTPException(status_code=404,detail=f"Recipe with id{recipe_id} not found")

    return result


# @api_router.get("/recipe/{recipe_id}",status_code=200)
# def fetch_recipie(*,recipe_id:int,include_total:bool=False) -> dict:
#     result = [recipe for recipe in RECIPES if recipe["id"] == recipe_id]

#     if result:
#         return result[0]

#     result = {}
#     if include_total:
#         result["total"] = len(RECIPES)
#     return result

@api_router.post("/recipe/",status_code=201,response_model=Recipe)
def create_recipe(*,recipe_in:RecipeCreate,db:session=Depends(deps.get_db)) -> dict:
    existing = crud.recipe.get_recipe_by_label_name(db=db,label=recipe_in.label)
    if existing:
        raise HTTPException(status_code=409,detail="Recipe already exists")
    
    recipe = crud.recipe.create(db=db,obj_in=recipe_in)
    return recipe

@api_router.get("/search",status_code=200,response_model=ReciepeSearchResults)
def search_recipe(*,keyword:Optional[str] = Query(None,min_length=3,examples=["Chicken"]),max_results:Optional[int]=10,db:session=Depends(deps.get_db)) -> dict:
    recipes = crud.recipe.get_multi(db=db,limit=max_results)

    if not keyword:
        return {"recipes": recipes}

    recipes = filter(lambda recipe: keyword.lower() in recipe.label.lower(),recipes)
    return {"recipes":recipes}

@app.router.delete("/recipe/{recipe_id}",status_code=204)
def delete_recipe(*,recipe_id,db:session=Depends(deps.get_db)) -> None:
    exists = crud.recipe.get(db=db,id=recipe_id)

    if not exists:
        raise HTTPException(status_code=404,detail=f"Recipe with id:{recipe_id} does not exists")

    crud.recipe.remove(db=db,id=recipe_id)

app.include_router(api_router)


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app",host="0.0.0.0",port=8001,log_level="debug",reload=True)