from facilyst.graphs import GraphBase
from facilyst.mock import Dates, Features, Target
from facilyst.utils.gen_utils import _get_subclasses

all_mock_data_types = [Dates, Features, Target]


def test_get_subclasses():

    print(_get_subclasses(GraphBase))
