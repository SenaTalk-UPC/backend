from pydantic import BaseModel

class TranslationDTO(BaseModel):
    id: int
    text: str
    folder_id: int
