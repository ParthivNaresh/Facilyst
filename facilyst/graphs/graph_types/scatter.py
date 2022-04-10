"""A graphing class to handle creating a scatter plot."""
import seaborn as sns

from facilyst.graphs import GraphBase


class Scatter(GraphBase):
    """Class to create a scatter plot.

    :param x: One dimensional data to be plotted on the x axis or the name of the column in the dataset. If the name of
    the column is passed, then dataset cannot be None.
    :type x: pd.Series, np.ndarray, or str
    :param y: One dimensional data to be plotted on the y axis or the name of the column in the dataset. If the name of
    the column is passed, then dataset cannot be None.
    :type y: pd.Series, np.ndarray, or str
    :param dataset: The dataset to which x and y correspond if x and y are column names.
    :type dataset: pd.DataFrame or np.ndarray, optional
    :param hue: Grouping variable that will produce points with different colors. Can be either categorical or numeric.
    :type hue: str or int, optional
    :param style: Grouping variable that will produce points with different markers. Can have a numeric dtype but will
    always be treated as categorical.
    :type style: str or int, optional
    :param plot_size: The size of the plot to create.
    :type plot_size: tuple, optional
    """

    name = "Scatterplot"

    def __init__(
        self, x=None, y=None, dataset=None, hue=None, style=None, plot_size=(11.7, 8.27)
    ):
        parameters = {"data": dataset, "x": x, "y": y, "hue": hue, "style": style}

        extra_parameters = {"plot_size": plot_size}

        sns_scatter = sns.scatterplot

        super().__init__(
            graph_obj=sns_scatter,
            parameters=parameters,
            extra_parameters=extra_parameters,
        )
