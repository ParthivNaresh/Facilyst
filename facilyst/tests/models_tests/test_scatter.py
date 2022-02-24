import numpy as np
import pandas as pd
import pytest
import seaborn as sns
import matplotlib.pyplot as plt

from facilyst.graphs import Scatter


def test_scatter():
    X = pd.DataFrame()
    X["x_axis"] = [i for i in range(10)]
    X["y_axis"] = [i for i in range(10)]

    scatter = Scatter(dataset=X, x="x_axis", y="y_axis")
    print(scatter)
    plt.show()
