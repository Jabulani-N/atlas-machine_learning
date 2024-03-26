#!/usr/bin/env python3
"""placeholder documentation"""


import tensorflow.keras as K


def preprocess_data(X, Y):
    """
    runs preprocessing on input dataset
    recieves a keras.datasets.datasetName.load_data()[i]
        which returns two objects when run
    """
    X_p = K.applications.efficientnet.preprocess_input(X)
    Y_p = K.utils.to_categorical(Y, 10)
    return X_p, Y_p
# the above preprocess_data() seems to work
def make_model():
    """
    makes an EfficientNetB7 model
    retrains it for the cifar10 dataset
    """
    # Load the CIFAR10 dataset
    (x_train, y_train), (x_test, y_test) = K.datasets.cifar10.load_data()

    # Preprocess the data using the preprocess_data function
    x_train, y_train = preprocess_data(x_train, y_train)
    x_test, y_test = preprocess_data(x_test, y_test)

    input_shape = (32, 32, 3)

    # Create the EfficientNetB7 model
    inputs = K.layers.Input(shape=input_shape)
    base_model = K.applications.EfficientNetB7(weights='imagenet', include_top=False, input_shape=input_shape, input_tensor=inputs)

    # Freezing
    base_model.trainable = False

    # Rebuild Top
    x = K.layers.GlobalAveragePooling2D(name="avg_pool")(base_model.output)
    x = K.layers.BatchNormalization()(x)
    x = K.layers.Dropout(0.25)(x)  # Dropout layer with a dropout rate of 0.25
    x = K.layers.Dense(256, activation='relu')(x)
    outputs = K.layers.Dense(10, activation='softmax')(x)  # Using 'outputs' for the final layer

    # Create the model
    model = K.Model(inputs=inputs, outputs=outputs, name="EfficientNet")

    # Compile the model
    optimizer = K.optimizers.Adam()
    model.compile(optimizer=optimizer, loss="categorical_crossentropy", metrics=["accuracy"])

    # Use the model to predict labels for the test data
    predictions = model.predict(x_test)

    # Convert the predictions to class labels
    predicted_labels = K.backend.argmax(predictions, axis=1)

    # Display the predicted labels
    print(predicted_labels)

    # Fit the model
    model.fit(x_train, y_train, batch_size=128, epochs=11, validation_data=(x_test, y_test))

if __name__ == '__main__':
    model = make_model()

