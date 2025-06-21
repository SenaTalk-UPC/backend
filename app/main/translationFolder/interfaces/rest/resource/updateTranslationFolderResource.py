from pydantic import BaseModel
from typing import List, Optional

class UpdateTranslationFolderResource(BaseModel):
    name: str
    description: Optional[str] = None
    translation_ids: List[int]
