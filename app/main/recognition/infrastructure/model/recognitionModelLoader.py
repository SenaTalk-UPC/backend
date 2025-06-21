from tensorflow.keras.models import load_model
import os
import numpy as np
import json

class RecognitionModelLoader:
    MODEL_PATH = "app/main/recognition/infrastructure/model/modelo_lsp.keras"
    ACTIONS_PATH = "app/main/recognition/infrastructure/model/actions.json"

    @staticmethod
    def load_model():
        return load_model(RecognitionModelLoader.MODEL_PATH)

    @staticmethod
    def load_actions():
        with open(RecognitionModelLoader.ACTIONS_PATH, 'r') as f:
            actions = json.load(f)
        return np.array(actions)
