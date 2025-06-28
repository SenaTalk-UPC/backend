from typing import List
import numpy as np

class Recognition:
    def __init__(self, actions: List[str], threshold: float = 0.5):
        self.sequence: List[List[float]] = []
        self.threshold = threshold
        self.actions = np.array(actions)
        self.sentence: List[str] = []

    def append_keypoints(self, keypoints: List[float]):
        self.sequence.append(keypoints)
        if len(self.sequence) > 30:
            self.sequence.pop(0)

    def is_ready(self) -> bool:
        return len(self.sequence) == 30

    def predict(self, model) -> dict:
        if not self.is_ready():
            return {"text": "", "confidence": 0.0}

        input_data = np.expand_dims(self.sequence, axis=0)
        if input_data.shape != (1, 30, 1662):
            raise ValueError(f"Expected input shape (1, 30, 1662), got {input_data.shape}")

        prediction = model.predict(input_data)[0]
        max_conf = np.max(prediction)
        predicted_action = self.actions[np.argmax(prediction)]

        if max_conf > self.threshold:
            if not self.sentence or predicted_action != self.sentence[-1]:
                self.sentence.append(predicted_action)
            if len(self.sentence) > 3:
                self.sentence = self.sentence[-3:]
            return {"text": " ".join(self.sentence), "confidence": float(max_conf)}

        return {"text": "", "confidence": float(max_conf)}
