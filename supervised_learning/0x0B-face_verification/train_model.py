#!/usr/bin/env python3
"""contains the TrainModel class"""

from triplet_loss import TripletLoss
import tensorflow as tf


class TrainModel:
    """
    TrainModel class
    """

    def __init__(self, model_path, alpha):
        """
        constructor
        :param model_path: path to the base face verification embedding model
            loads the model using with tf.keras.utils.CustomObjectScope({'tf': tf}):
            saves this model as the public instance method base_model
        :param alpha: alpha to use for the triplet loss calculation
        """
        #with tf.keras.utils.CustomObjectScope({'tf': tf}):
        self.training_model = tf.keras.models.load_model(model_path)

        #self.base_model.summary()
        """
        self.base_model.save('base_model')
        

        A = tf.placeholder(tf.float32, (None, 96, 96, 3))
        P = tf.placeholder(tf.float32, (None, 96, 96, 3))
        N = tf.placeholder(tf.float32, (None, 96, 96, 3))
        inputs = [A, P, N]

        output = self.base_model(inputs)
        tl = TripletLoss(alpha)
        output = tl(output)

        self.training_model = tf.keras.models.Model(inputs, output)

        self.training_model.compile(optimizer='Adam')

        self.training_model.save('training_model')
        """
    def train(self, triplets, epochs=5, batch_size=32, validation_split=0.3, verbose=True):
        """

        :param triplets: list containing the inputs to self.training_model
        :param epochs: number of epochs to train for
        :param batch_size: batch size for training
        :param validation_split: validation split for training
        :param verbose: boolean that sets the verbosity mode
        :return: History output from the training
        """
        # training
        history = self.training_model.fit(triplets,
                                          batch_size=batch_size,
                                          epochs=epochs,
                                          verbose=verbose,
                                          validation=validation_split)

        return history

    def save(self, save_path):
        """

        :param save_path: path to save the model
        :return: saved model
        """
        self.base_model.save(save_path)

    @staticmethod
    def f1_score(y_true, y_pred):
        """

        :param y_true:
        :param y_pred:
        :return: the f1 score
        """

    @staticmethod
    def accuracy(y_true, y_pred):
        """

        :param y_true:
        :param y_pred:
        :return: the accuracy
        """

    def best_tau(self, images, identities, thresholds):
        """

        :param images:
        :param identities:
        :param thresholds:
        :return: (tau, f1, acc)
        """