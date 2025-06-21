from pydantic import BaseModel

class TranslationDTO(BaseModel):
    id: int
    user_email: str
    text: str
