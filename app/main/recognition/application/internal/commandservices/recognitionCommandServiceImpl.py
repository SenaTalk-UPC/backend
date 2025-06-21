import numpy as np
from typing import List
from app.main.recognition.domain.services.recognitionCommandService import RecognitionCommandService
from app.main.recognition.domain.model.aggregates.recognition import Recognition

class RecognitionCommandServiceImpl(RecognitionCommandService):
    def __init__(self, model, actions):
        self.model = model
        self.actions = actions
        self.threshold = 0.5

    def recognize(self, sequence: List[List[float]]) -> Recognition:
        if len(sequence) != 30 or len(sequence[0]) != 1662:
            raise ValueError("La secuencia debe tener shape (30, 1662)")

        X = np.expand_dims(np.array(sequence), axis=0)  # Shape: (1, 30, 1662)
        res = self.model.predict(X)[0]
        prediction_index = np.argmax(res)
        confidence = res[prediction_index]
        recognized_word = self.actions[prediction_index]

        return Recognition(recognized_word=recognized_word, confidence=float(confidence))
