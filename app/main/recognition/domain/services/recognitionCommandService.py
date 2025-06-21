from abc import ABC, abstractmethod
from typing import List
from app.main.recognition.domain.model.aggregates.recognition import Recognition

class RecognitionCommandService(ABC):

    @abstractmethod
    def recognize(self, sequence: List[List[float]]) -> Recognition:
        pass
