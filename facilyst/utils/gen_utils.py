def _get_subclasses(base_class):
    classes_to_check = base_class.__subclasses__()

    subclasses = []

    while classes_to_check:
        subclass = classes_to_check.pop()
        subclasses.append(subclass)

    return subclasses


def handle_problem_type(problem_type):
    """Handles the problem type passed to be returned in a consistent way.

    :param problem_type: The problem type to match.
    :type problem_type: str
    """
    if problem_type.lower() in ["regression"]:
        problem_type_ = "regression"
    elif problem_type.lower() in ["binary"]:
        problem_type_ = "binary"
    elif problem_type.lower() in ["multiclass"]:
        problem_type_ = "multiclass"
    elif problem_type.lower() in [
        "time series regression",
        "timeseries regression",
        "ts regression",
    ]:
        problem_type_ = "time series regression"
    else:
        raise ValueError("That problem type isn't recognized!")

    return problem_type_
