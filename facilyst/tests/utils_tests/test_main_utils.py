from unittest.mock import patch

from facilyst.utils import make_dates, make_features, make_wave


@patch("facilyst.utils.main_utils.create_data")
def test_make_features(mock_create_data):
    mock_features = make_features(
        num_rows=1000, library="numpy", booleans=True, floats_with_na=True
    )
    mock_create_data.assert_called_once_with(
        "features",
        num_rows=1000,
        library="numpy",
        ints=True,
        rand_ints=True,
        floats=True,
        rand_floats=True,
        booleans=True,
        categoricals=False,
        dates=False,
        texts=False,
        ints_with_na=False,
        floats_with_na=True,
        all_dtypes=False,
    )


@patch("facilyst.utils.main_utils.create_data")
def test_make_dates(mock_create_data):
    mock_features = make_dates(
        num_rows=500, library="numpy", start_date="05/13/1989", misaligned=True
    )
    mock_create_data.assert_called_once_with(
        "dates",
        num_rows=500,
        library="numpy",
        start_date="05/13/1989",
        frequency="1D",
        missing=False,
        misaligned=True,
        duplicates=False,
        chaos=1,
    )


@patch("facilyst.utils.main_utils.create_data")
def test_make_wave(mock_create_data):
    mock_features = make_wave(
        num_rows=2000, library="numpy", wave_type="cosine", random_amplitudes=True
    )
    mock_create_data.assert_called_once_with(
        "wave",
        num_rows=2000,
        library="numpy",
        wave_type="cosine",
        amplitude=1,
        frequency=1,
        random_amplitudes=True,
        random_frequency=False,
        trend=0.0,
    )
