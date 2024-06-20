#!/usr/bin/env python3
"""task 2"""


import tensorflow.keras as keras


def autoencoder(input_dims, filters, latent_dims):
    """creates an autoencoder

    input_dims = tuple of integers
        contains dimensions of the model input
            unlike previous tasks, already intuple form
    filters = list
        contains number of filters for each convolutional layer in the encoder
            filters should be reversed from given order for the decoder
    latent_dims = tuple of integers
        contains dimensions of the latent space representation
    """
    # we use this input layer later, so it needs to be unique
    encoder_input = keras.Input(shape=input_dims)
    # must be defined this way
    encoded = encoder_input

    for filter in filters:
        encoded = keras.layers.Conv2D(filter, (3, 3),
                                      activation='relu',
                                      padding='same')(encoded)
        encoded = keras.layers.MaxPooling2D((2, 2),
                                            padding='same')(encoded)

    encoder_output = encoded
    encoder = keras.Model(encoder_input, encoder_output)

    # as above, we need the unique input one
    decoder_input = keras.Input(shape=latent_dims)
    # must be defined this way
    decoded = decoder_input
    for i in range(len(filters) - 1, -1, -1):
        if i == 0:
            padding = 'valid'
        else:
            padding = 'same'

        decoded = keras.layers.Conv2D(filters[i],
                                      (3, 3),
                                      activation='relu',
                                      padding=padding)(decoded)
        decoded = keras.layers.UpSampling2D((2, 2))(decoded)

    decoder_output = keras.layers.Conv2D(input_dims[-1],
                                         (3, 3),
                                         activation='sigmoid',
                                         padding='same')(decoded)
    decoder = keras.Model(decoder_input,
                          decoder_output)

    # Define the full autoencoder model
    # autoencoder_input = keras.Input(shape=input_dims)
    # encoded_output = encoder(autoencoder_input)
    # decoded_output = decoder(encoded_output)
    # auto = keras.Model(autoencoder_input, decoded_output, name='autoencoder')
    # trying a literal logical part here that should be unable to be wrong
    auto = keras.Model(encoder_input,
                       decoder(encoder(encoder_input)))

    # Compile the autoencoder model
    auto.compile(optimizer='adam', loss='binary_crossentropy')

    return encoder, decoder, auto
