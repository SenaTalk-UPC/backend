from pydantic import BaseModel, EmailStr

class TranslationResource(BaseModel):
    id: int
    text: str
    folder_id: int
