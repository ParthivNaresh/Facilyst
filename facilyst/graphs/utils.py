from facilyst.graphs import GraphBase
from facilyst.utils.gen_utils import _get_subclasses


def _all_graph_data_types():
    return _get_subclasses(GraphBase)