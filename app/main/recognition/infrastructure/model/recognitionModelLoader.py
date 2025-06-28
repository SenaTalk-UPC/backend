import os
import numpy as np
import tensorflow as tf

class RecognitionModelLoader:
    def __init__(self):
        # Carga del modelo
        self.model = tf.keras.models.load_model('app/main/recognition/infrastructure/model/model_lsp.keras')

        # Acciones entrenadas
        self.actions = np.array([
            'hola', 'jugar', 'a', 'e', 'gracias', 'ir', 'yo', 'neutral', 'tu',
            'donde', 'dias', 'adios', 'nombre', 'de nada', 'ordenar', 'guardar'
        ])

    def get_model(self):
        return self.model

    def get_actions(self):
        return self.actions
