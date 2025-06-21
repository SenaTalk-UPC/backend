from pydantic import BaseModel

class SignInResource(BaseModel):
    email: str
    password: str
