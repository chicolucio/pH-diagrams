def is_sorted(lst):
    return all(a <= b for a, b in zip(lst, lst[1:]))


def next_smaller(lst):
    last_item = None
    i = 0
    for index, item in enumerate(lst):
        if last_item is None or (item >= last_item and index == i):
            last_item = item
            i += 1
            yield item


def valid_pka_values(values):
    """
    This function filters possible pKa values for the app web page.
    It's perfectly fine negative pKa values and non-sorted values in real life
    but is not so usual. Then, for educational purposes, it was decided to
    create this filter.

    Parameters
    ----------
    values : tuple

    Returns
    -------
    list

    """
    values = list(values)
    if is_sorted(values):
        result = values
    else:
        result = list(next_smaller(values))
    return result
