from facilyst.mocks import Dates, Features, MockBase, Target
from facilyst.utils.gen_utils import _get_subclasses

all_mock_data_types = [Dates, Features, Target]


def test_mock_data_children():
    all_mock_types = {mock_type.__name__ for mock_type in all_mock_data_types}
    all_subclasses = {subclass.__name__ for subclass in _get_subclasses(MockBase)}
    assert all_mock_types == all_subclasses
