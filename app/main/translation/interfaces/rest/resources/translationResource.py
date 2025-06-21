from pydantic import BaseModel, EmailStr

class TranslationResource(BaseModel):
    id: int
    user_email: str
    text: str
