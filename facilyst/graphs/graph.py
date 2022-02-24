from abc import ABC, abstractmethod

from matplotlib import rcParams
import woodwork as ww


class Graph(ABC):
    def __init__(self, graph_obj, parameters, extra_parameters):
        self.parameters = parameters
        self.extra_parameters = extra_parameters
        self.check_x_y()

        self.graph_obj = graph_obj(**self.parameters)

    @property
    @abstractmethod
    def name(self):
        "Name of the graph"

    def resize(self, width=11.7, height=8.27):
        rcParams["figure.figsize"] = width, height

    def show(self):
        pass

    def handle_x_y(self):
        pass

    def check_x_y(self):
        if self.parameters["data"] is None:
            if isinstance(self.parameters["x"], str) or isinstance(
                self.parameters["y"], str
            ):
                raise ValueError(
                    "If dataset is None, then x and y need to contain a collection of data!"
                )
        else:
            if not (
                isinstance(self.parameters["x"], str)
                and isinstance(self.parameters["y"], str)
            ):
                raise ValueError(
                    "If dataset is not None, then x and y need to be strings referring to column names in dataset!"
                )
            if self.parameters["x"] not in self.parameters["data"].columns:
                raise ValueError(
                    f"Column {self.parameters['x']} could not be found in the dataset columns!"
                )
            elif self.parameters["y"] not in self.parameters["data"].columns:
                raise ValueError(
                    f"Column {self.parameters['y']} could not be found in the dataset columns!"
                )
