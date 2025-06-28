import tensorflow as tf

model = tf.keras.models.load_model("app/main/recognition/infrastructure/model/model_lsp.keras")
actions = ["hola", "jugar", "a", "e", "gracias", "ir","yo", "neutral","tu","donde", "dias", "adios", "nombre", "de nada", "ordenar", "guardar"]
