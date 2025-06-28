from pydantic import BaseModel, EmailStr

class CreateTranslationResource(BaseModel):
    text: str
    folder_id: int
