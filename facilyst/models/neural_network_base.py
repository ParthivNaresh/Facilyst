"""Base class for neural network models."""
from abc import ABC, abstractmethod

import pandas as pd


class NeuralNetworkBase(ABC):
    """Base initialization for all mock types.

    :param model: The neural network-based model to be used.
    :type model: object
    """

    def __init__(self, model=None):
        self.model = model

    @property
    @abstractmethod
    def name(self):
        """Name of the model."""

    def fit(self, x_train, y_train):
        """Fits model to the data.

        :param x_train: The training data for the model to be fitted on.
        :type x_train: pd.DataFrame or np.ndarray
        :param y_train: The training targets for the model to be fitted on.
        :type y_train: pd.Series or np.ndarray
        """
        self.model.fit(x_train, y_train)
        return self

    def predict(self, x_test):
        """Predicts on the data using the model.

        :param x_test: The testing data for the model to predict on.
        :type x_test: pd.DataFrame or np.ndarray
        """
        predictions = pd.Series(self.model.predict(x_test))
        return predictions

    def score(self, x_test, y_actual):
        """Scores the predictions of the model using R2.

        :param x_test: The testing data for the model to predict on.
        :type x_test: pd.DataFrame or np.ndarray
        :param y_actual: The actual target values to score against.
        :type y_actual: pd.Series or np.ndarray
        """
        score = self.model.score(x_test, y_actual)
        return score

    def get_params(self):
        """Gets the parameters for the model."""
        model_params = self.model.get_params(deep=True)
        return model_params
