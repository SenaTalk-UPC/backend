from app.main.recognition.domain.services.recognitionQueryService import RecognitionQueryService
from app.main.recognition.domain.model.aggregates.recognition import Recognition
from app.main.recognition.infrastructure.model.recognitionModelLoader import model, actions
import numpy as np

class RecognitionQueryServiceImpl(RecognitionQueryService):
    def __init__(self):
        self.sequence = []
        self.threshold = 0.5
        self.last_prediction = ""

    def predict(self, keypoints: list[float]) -> Recognition:
        self.sequence.append(keypoints)
        if len(self.sequence) > 30:
            self.sequence.pop(0)

        if len(self.sequence) == 30:
            res = model.predict(np.expand_dims(self.sequence, axis=0))[0]
            confidence = float(max(res))
            action = actions[np.argmax(res)]

            if confidence > self.threshold:
                self.last_prediction = action
                return Recognition(text=action, confidence=confidence)

        return Recognition(text=self.last_prediction, confidence=0.0)
