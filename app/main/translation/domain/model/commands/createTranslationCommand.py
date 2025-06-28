from pydantic import BaseModel, EmailStr

class CreateTranslationCommand(BaseModel):
    text: str
    folder_id: int
