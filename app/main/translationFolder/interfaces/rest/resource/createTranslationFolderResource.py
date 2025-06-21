from pydantic import BaseModel
from typing import List

class CreateTranslationFolderResource(BaseModel):
    name: str
    description: str
    translation_ids: List[int]