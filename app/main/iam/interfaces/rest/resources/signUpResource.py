from pydantic import BaseModel

class SignUpResource(BaseModel):
    email: str
    password: str
