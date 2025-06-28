from pydantic import BaseModel

class SignUpResource(BaseModel):
    username: str
    email: str
    password: str
