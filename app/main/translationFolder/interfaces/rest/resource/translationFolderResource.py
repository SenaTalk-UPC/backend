from pydantic import BaseModel
from typing import List

class TranslationFolderResource(BaseModel):
    id: int
    name: str
    description: str
    userId: int
