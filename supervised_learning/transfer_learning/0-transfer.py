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

    # Create the EfficientNetB7 model
    model = K.applications.EfficientNetB7(weights='imagenet', include_top=True)

if __name__ == '__main__':
    madeModel = make_model()