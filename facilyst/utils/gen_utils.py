def _get_subclasses(base_class):
    classes_to_check = base_class.__subclasses__()

    subclasses = []

    while classes_to_check:
        subclass = classes_to_check.pop()
        children = subclass.__subclasses__()

        if children:
            classes_to_check.extend(children)
        else:
            subclasses.append(subclass)

    return subclasses
