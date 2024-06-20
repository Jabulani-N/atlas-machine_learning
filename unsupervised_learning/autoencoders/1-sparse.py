#!/usr/bin/env python3
"""task 1"""


import tensorflow.keras as keras


def autoencoder(input_dims, hidden_layers, latent_dims, lambtha):
    """creates an autoencoder

    input_dims = integer
        contains dimensions of the model input
    hidden_layers = list
        contains number of nodes
            for each hidden layer in encoder, respectively
    lambtha = regularization parameter
        used for L1 regularization on  encoded output
    the hidden layers should be reversed for the decoder
    latent_dims = integer
        contains dimensions of the latent space representation
    """
    # return None
    # we use this input layer later, so it needs to be unique
    encoder_input = keras.Input(shape=(input_dims,))
    # must be defined this way
    encoded = encoder_input
    for nodes in hidden_layers:
        encoded = keras.layers.Dense(nodes,
                                     activation='relu')(encoded)
    # insert activity regularizer to this line from task 0
    encoder_output =\
        keras.layers.Dense(latent_dims,
                           activation='relu',
                           activity_regularizer=keras.regularizers.l1(lambtha)
                           )(encoded)
    encoder = keras.Model(encoder_input, encoder_output,
                          name='encoder')

    # as above, we need the unique input one
    decoder_input = keras.Input(shape=(latent_dims,))
    # must be defined this way
    decoded = decoder_input
    for nodes in reversed(hidden_layers):
        decoded = keras.layers.Dense(nodes,
                                     activation='relu')(decoded)
    decoder_output = keras.layers.Dense(input_dims,
                                        activation='sigmoid')(decoded)
    decoder = keras.Model(decoder_input, decoder_output, name='decoder')

    # Define the full autoencoder model
    autoencoder_input = keras.Input(shape=(input_dims,))
    encoded_output = encoder(autoencoder_input)
    decoded_output = decoder(encoded_output)
    auto = keras.Model(autoencoder_input, decoded_output, name='autoencoder')

    # Compile the autoencoder model
    auto.compile(optimizer='adam', loss='binary_crossentropy')

    return encoder, decoder, auto
