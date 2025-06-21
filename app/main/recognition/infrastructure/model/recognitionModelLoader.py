from tensorflow.keras.models import load_model
import numpy as np
import json
import os

class RecognitionModelLoader:
    MODEL_PATH = "app/main/recognition/infrastructure/model/model_lsp.keras"
    ACTIONS_PATH = "app/main/recognition/infrastructure/model/actions.json"

    @staticmethod
    def load_model():
        if not os.path.exists(RecognitionModelLoader.MODEL_PATH):
            raise FileNotFoundError(f"Modelo no encontrado en {RecognitionModelLoader.MODEL_PATH}")
        return load_model(RecognitionModelLoader.MODEL_PATH)

    @staticmethod
    def load_actions():
        if not os.path.exists(RecognitionModelLoader.ACTIONS_PATH):
            raise FileNotFoundError(f"Archivo de acciones no encontrado en {RecognitionModelLoader.ACTIONS_PATH}")
        with open(RecognitionModelLoader.ACTIONS_PATH, 'r', encoding='utf-8') as f:
            actions = json.load(f)
        return np.array(actions)
