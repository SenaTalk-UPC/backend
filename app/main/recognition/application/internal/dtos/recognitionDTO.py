from pydantic import BaseModel

class RecognitionDTO(BaseModel):
    prediction: str
    confidence: float
