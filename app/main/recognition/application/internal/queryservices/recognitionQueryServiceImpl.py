from app.main.recognition.domain.services.commandService import RecognitionCommandService
from app.main.recognition.domain.model.aggregates.recognition import Recognition
from app.main.recognition.infrastructure.model.recognitionModelLoader import RecognitionModelLoader
import numpy as np

class RecognitionCommandServiceImpl(RecognitionCommandService):
    def __init__(self):
        self.model = RecognitionModelLoader.load_model()
        self.actions = RecognitionModelLoader.load_actions()
        self.threshold = 0.5

    def recognize(self, keypoints_sequence: list[list[float]]) -> Recognition:
        if len(keypoints_sequence) != 30:
            raise ValueError("La secuencia debe tener exactamente 30 frames")

        sequence_np = np.expand_dims(np.array(keypoints_sequence), axis=0)
        predictions = self.model.predict(sequence_np)[0]

        max_index = int(np.argmax(predictions))
        confidence = float(predictions[max_index])
        action = self.actions[max_index]

        if confidence < self.threshold:
            action = "Desconocido"

        return Recognition(prediction=action, confidence=confidence)
