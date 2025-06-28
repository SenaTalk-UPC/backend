from pydantic import BaseModel
from typing import List

class RecognitionRequestResource(BaseModel):
    keypoints: List[float]

class RecognitionResponseResource(BaseModel):
    text: str
    confidence: float
