
from pydantic import BaseModel, EmailStr, Field

class RegisterDTO(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6)
