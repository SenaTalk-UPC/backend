from pydantic import BaseModel
from typing import List

class RecognitionResource(BaseModel):
    sequence: List[List[float]]
