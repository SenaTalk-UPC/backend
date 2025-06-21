from pydantic import BaseModel
from typing import List

class TranslationFolderDTO(BaseModel):
    id: int
    name: str
    translation_ids: List[int]
