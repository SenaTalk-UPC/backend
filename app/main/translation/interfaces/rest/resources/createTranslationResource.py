from pydantic import BaseModel, EmailStr

class CreateTranslationResource(BaseModel):
    user_email: str
    text: str
