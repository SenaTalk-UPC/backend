from pydantic import BaseModel, EmailStr

class CreateTranslationCommand(BaseModel):
    user_email: str
    text: str
