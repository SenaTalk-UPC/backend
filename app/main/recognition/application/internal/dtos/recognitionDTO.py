# app/main/recognition/application/internal/dtos/recognitionDTO.py
from pydantic import BaseModel
from typing import List

class RecognitionRequest(BaseModel):
    keypoints: List[List[float]]

class RecognitionResponse(BaseModel):
    text: str
    confidence: float
