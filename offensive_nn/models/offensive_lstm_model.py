import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


class OffensiveLSTMModel:

    def __init__(self, args, embedding_matrix):
        inp = tf.keras.Input(shape=(None,), dtype="int64", name="input")
        x = layers.Embedding(args.max_features, args.embed_size,
                             embeddings_initializer=keras.initializers.Constant(embedding_matrix), trainable=False,
                             name="embedding_layer")(inp)
        x = layers.Bidirectional(layers.LSTM(64, return_sequences=True, name="lstm_1"))(x)
        x = layers.Bidirectional(layers.LSTM(64, name="lstm_2"))(x)
        x = layers.Dense(256, activation="relu", name="dense_1")(x)
        x = layers.Dense(args.num_classes, activation="softmax", name="dense_predictions")(x)
        self.model = tf.keras.Model(inputs=inp, outputs=x, name="lstm_model")
