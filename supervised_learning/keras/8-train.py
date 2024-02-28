#!/usr/bin/env python3
"""this module creates a function."""


import tensorflow.keras as K


def train_model(network, data, labels,
                batch_size, epochs, validation_data=None,
                early_stopping=False, patience=0,
                learning_rate_decay=False, alpha=0.1, decay_rate=1,
                save_best=False, filepath=None, verbose=True, shuffle=False):
    """
    New features:
    save_best = whether to save  model after each epoch if it is best
        model is best if validation loss is the lowest yet
    filepath is the file path where the model should be saved
    """

    callbacks = []
    decay_steps = 1

    if save_best:
        chk = K.callbacks.ModelCheckpoint(filepath,
                                          monitor="val_loss",
                                          save_best_only=True)
        callbacks.append(chk)

    if validation_data is not None and learning_rate_decay:
        schedule = K.optimizers.schedules.InverseTimeDecay(alpha,
                                                           decay_steps,
                                                           decay_rate,
                                                           staircase=True)
        callbacks.append(K.callbacks.LearningRateScheduler(schedule,
                                                           verbose=1))

    if validation_data is not None and early_stopping and patience < epochs:
        callbacks.append(K.callbacks.EarlyStopping(patience=patience))

    return network.fit(data, labels, batch_size=batch_size,
                       epochs=epochs, verbose=verbose,
                       shuffle=shuffle, validation_data=validation_data,
                       callbacks=callbacks)
