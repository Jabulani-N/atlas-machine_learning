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
    save_best = boolean for whether to save the model after each epoch if it is the best
        model is the best if its validation loss is the lowest the model has obtained
    filepath is the file path where the model should be saved
    """


    callbacks = []
    decay_steps = 1

    if save_best:
        chk = K.callbacks.ModelCheckpoint(filepath, monitor="val_loss", save_best_only=True)
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
