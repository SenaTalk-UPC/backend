from abc import ABC, abstractmethod
from app.main.recognition.domain.model.aggregates.recognition import Recognition

class RecognitionQueryService(ABC):
    @abstractmethod
    def predict(self, keypoints: list[float]) -> Recognition:
        pass
