from typing import Type,Optional,List,Any
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session


from app.crud.base import CRUDBase
from app.models.recipe import Recipe
from app.schemas.recipe import RecipeCreate,RecipeUpdate

class CRUDRecipe(CRUDBase[Recipe,RecipeCreate,RecipeUpdate]):

    def get_recipe_by_label_name(self,db:Session,label:str) -> Optional[Recipe]:
        return db.query(self.model).filter(self.label.ilike(f"%{label}%")).first()

recipe = CRUDRecipe(Recipe)