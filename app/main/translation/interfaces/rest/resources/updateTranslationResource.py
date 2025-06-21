from pydantic import BaseModel

class UpdateTranslationResource(BaseModel):
    text: str
