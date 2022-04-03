from facilyst.graphs import GraphBase, Line, Scatter
from facilyst.mocks import Dates, Features, MockBase, Wave
from facilyst.utils import _get_subclasses

expected_mock_subclasses = [
    Wave,
    Features,
    Dates,
]

expected_graph_subclasses = [
    Scatter,
    Line,
]


def test_mock_get_subclasses():
    actual_mock_subclasses = _get_subclasses(MockBase)
    assert actual_mock_subclasses == expected_mock_subclasses


def test_graph_get_subclasses():
    actual_graph_subclasses = _get_subclasses(GraphBase)
    assert actual_graph_subclasses == expected_graph_subclasses
