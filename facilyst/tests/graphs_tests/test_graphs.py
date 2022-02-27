import matplotlib
import numpy as np
import pandas as pd
import pytest

from facilyst.graphs import Scatter


@pytest.mark.parametrize("dataset_type", ["pandas", "numpy", "list", None])
@pytest.mark.parametrize(
    "x_type", ["pandas", "numpy", "list", "str_valid", "str_invalid", None]
)
@pytest.mark.parametrize(
    "y_type", ["pandas", "numpy", "list", "str_valid", "str_invalid", None]
)
def test_warnings(dataset_type, x_type, y_type):
    data_ = [[i for i in range(10)] for j in range(10)]

    if dataset_type == "pandas":
        dataset = pd.DataFrame(data_)
    elif dataset_type == "numpy":
        dataset = np.array(data_)
    elif dataset_type == "list":
        dataset = data_
    else:
        dataset = None

    if x_type == "pandas":
        x = pd.DataFrame(data_)
    elif x_type == "numpy":
        x = np.array(data_)
    elif x_type == "list":
        x = data_
    elif x_type == "str_valid":
        x = "1"
    elif x_type == "str_invalid":
        x = "11"
    else:
        x = None

    if y_type == "pandas":
        y = pd.Series([i for i in range(10)])
    elif y_type == "numpy":
        y = np.array([i for i in range(10)])
    elif y_type == "list":
        y = [i for i in range(10)]
    elif y_type == "str_valid":
        y = "2"
    elif y_type == "str_invalid":
        y = "11"
    else:
        y = None

    if dataset_type is None and (
        x_type in ["str_valid", "str_invalid", None]
        or y_type in ["str_valid", "str_invalid", None]
    ):
        with pytest.raises(
            ValueError,
            match="If `dataset` is None, then `x` and `y` need to contain a collection of data!",
        ):
            Scatter(dataset=dataset, x=x, y=y)
    elif dataset_type in ["pandas", "numpy", "list"] and (
        x_type not in ["str_valid", "str_invalid"]
        or y_type not in ["str_valid", "str_invalid"]
    ):
        with pytest.raises(
            ValueError,
            match="If `dataset` is not None, then `x` and `y` need to be strings referring to column names in dataset!",
        ):
            Scatter(dataset=dataset, x=x, y=y)
    elif dataset_type == "pandas" and x_type == "str_invalid":
        with pytest.raises(
            ValueError, match=f"Column {x} could not be found in the `dataset` columns!"
        ):
            Scatter(dataset=dataset, x=x, y=y)
    elif dataset_type == "pandas" and x_type == "str_valid" and y_type == "str_invalid":
        with pytest.raises(
            ValueError, match=f"Column {y} could not be found in the `dataset` columns!"
        ):
            Scatter(dataset=dataset, x=x, y=y)
    elif dataset_type != "pandas" and (
        x_type == "str_invalid" or (x_type == "str_valid" and y_type == "str_invalid")
    ):
        with pytest.raises(
            ValueError,
            match="If `dataset` is not of pandas type, then `x` and `y` have to be strings "
            "corresponding to the column location e.g. '0', '1', '2', etc.",
        ):
            Scatter(dataset=dataset, x=x, y=y)
    else:
        Scatter(dataset=dataset, x=x, y=y)


@pytest.mark.parametrize("x_type", ["pandas", "numpy", "list", "None"])
@pytest.mark.parametrize("y_type", ["pandas", "numpy", "list", "None"])
def test_warnings_without_dataset(x_type, y_type, one_dim_data):
    if x_type not in ["pandas", "numpy"]:
        with pytest.raises(
            ValueError,
            match="If `dataset` is None, then `x` must be a collection of data of type pd.Series or np.ndarray!",
        ):
            _ = Scatter(dataset=None, x=one_dim_data[x_type], y=one_dim_data[y_type])
    elif y_type not in ["pandas", "numpy"]:
        with pytest.raises(
            ValueError,
            match="If `dataset` is None, then `y` must be a collection of data of type pd.Series or np.ndarray!",
        ):
            _ = Scatter(dataset=None, x=one_dim_data[x_type], y=one_dim_data[y_type])
    else:
        _ = Scatter(dataset=None, x=one_dim_data[x_type], y=one_dim_data[y_type])


@pytest.mark.parametrize("dataset_type", ["pandas", "numpy", "list"])
@pytest.mark.parametrize("x_type", ["pandas", "numpy", "list", "str", "None"])
@pytest.mark.parametrize("y_type", ["pandas", "numpy", "list", "str", "None"])
def test_warnings_with_dataset(
    dataset_type, x_type, y_type, multi_dim_data, one_dim_data
):
    if dataset_type not in ["pandas", "numpy"]:
        with pytest.raises(
            ValueError, match="`dataset` must be of type pd.DataFrame or np.ndarray!"
        ):
            _ = Scatter(
                dataset=multi_dim_data[dataset_type],
                x=one_dim_data[x_type],
                y=one_dim_data[y_type],
            )
    elif x_type not in ["str", "None"] or y_type not in ["str", "None"]:
        with pytest.raises(
            ValueError,
            match="If `dataset` is not None, then `x` and `y` need to be hashable values referring to column names in dataset!",
        ):
            _ = Scatter(
                dataset=multi_dim_data[dataset_type],
                x=one_dim_data[x_type],
                y=one_dim_data[y_type],
            )
    elif x_type == "None" or y_type == "None":
        with pytest.raises(ValueError, match="`x` and `y` cannot be None!"):
            _ = Scatter(
                dataset=multi_dim_data[dataset_type],
                x=one_dim_data[x_type],
                y=one_dim_data[y_type],
            )
    else:
        _ = Scatter(
            dataset=multi_dim_data[dataset_type],
            x=one_dim_data[x_type],
            y=one_dim_data[y_type],
        )


@pytest.mark.parametrize("dataset_type", ["pandas", "numpy"])
@pytest.mark.parametrize("x_name", [0, 11])
@pytest.mark.parametrize("y_name", [0, 11])
def test_column_not_in_dataset(dataset_type, x_name, y_name, multi_dim_data):
    if x_name == 11 or y_name == 11:
        with pytest.raises(
            ValueError,
            match="Column `11` could not be found in the `dataset` columns! If you passed in a "
            "dataset of type np.ndarray, use an integer to indicate the column number e.g. 0, 1, 2, etc. "
            "`dataset` has 10 columns.",
        ):
            _ = Scatter(dataset=multi_dim_data[dataset_type], x=x_name, y=y_name)
    else:
        _ = Scatter(dataset=multi_dim_data[dataset_type], x=x_name, y=y_name)


def test_default_size_and_resize(multi_dim_data):
    dataset = multi_dim_data["pandas"]

    scatter = Scatter(x=0, y=1, dataset=dataset)
    assert np.array_equal(scatter.get_size(), np.array([11.7, 8.27]))

    scatter.resize(20, 10)
    assert np.array_equal(scatter.get_size(), np.array([20, 10]))


def test_get_figure(multi_dim_data):
    dataset = multi_dim_data["pandas"]

    scatter = Scatter(x=0, y=1, dataset=dataset)
    assert isinstance(scatter.get_figure()(), matplotlib.figure.Figure)
