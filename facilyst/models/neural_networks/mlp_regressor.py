from sklearn.neural_network import MLPRegressor

from facilyst.models.neural_network_base import NeuralNetworkBase


class MultiLayerPerceptronRegressor(NeuralNetworkBase):

    name = "Multilayer Perceptron"

    def __init__(
        self,
        hidden_layer_sizes=(100,),
        activation="relu",
        solver="adam",
        alpha=0.0001,
        batch_size="auto",
        learning_rate="constant",
        learning_rate_init=0.001,
        max_iter=200,
    ):

        parameters = {
            "hidden_layer_sizes": hidden_layer_sizes,
            "activation": activation,
            "solver": solver,
            "alpha": alpha,
            "batch_size": batch_size,
            "learning_rate": learning_rate,
            "learning_rate_init": learning_rate_init,
            "max_iter": max_iter,
        }

        multilayer_perceptron_model = MLPRegressor(**parameters)

        super().__init__(model=multilayer_perceptron_model)
