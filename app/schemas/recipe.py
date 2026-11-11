from pydantic import BaseModel,HttpUrl,ConfigDict
from typing import Sequence


class RecipeBase(BaseModel):
    label: str
    source: str
    url: HttpUrl


class RecipeCreate(RecipeBase):
    label: str
    source: str
    url: HttpUrl
    submitter_id: int


class RecipeUpdate(RecipeBase):
    label: str


class RecipeInDBBase(RecipeBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    submitter_id: int


class Recipe(RecipeInDBBase):
    pass


class RecipeInDB(RecipeInDBBase):
    pass


class ReciepeSearchResults(BaseModel):
    results: Sequence[RecipeBase]