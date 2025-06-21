from abc import ABC, abstractmethod
from app.main.recognition.domain.model.aggregates.recognition import Recognition

class RecognitionCommandService(ABC):
    @abstractmethod
    def recognize(self, keypoints_sequence: list[list[float]]) -> Recognition:
        pass
