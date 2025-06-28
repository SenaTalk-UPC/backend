# app/main/recognition/application/internal/queryservices/recognitionQueryServiceImpl.py
from app.main.recognition.domain.model.aggregates.recognition import Recognition
from app.main.recognition.infrastructure.model.recognitionModelLoader import RecognitionModelLoader

class RecognitionQueryServiceImpl:
    def __init__(self):
        loader = RecognitionModelLoader()
        self.model = loader.get_model()
        self.actions = loader.get_actions()
        self.recognition = Recognition(self.actions)

    def predict(self, keypoints_sequence: list) -> dict:
        for keypoints in keypoints_sequence:
            self.recognition.append_keypoints(keypoints)
        return self.recognition.predict(self.model)
