from pydantic import BaseModel

class AuthenticatedUserResource(BaseModel):
    email: str
    token: str
