import pytest

from facilyst.mocks.mock_types import handle_data_and_library_type


@pytest.mark.parametrize(
    "data_type", ["dataframe", "features", "series", "target", "x", "y"]
)
@pytest.mark.parametrize("library", ["pandas", "numpy", "pd", "np"])
def test_handle_data_and_library_type(data_type, library):
    data_type_, library_ = handle_data_and_library_type(data_type, library)
    if data_type in ["dataframe", "features", "x"]:
        assert data_type_ == "features"
    else:
        assert data_type_ == "target"
    if library in ["pandas", "pd"]:
        assert library_ == "pandas"
    else:
        assert library_ == "numpy"
