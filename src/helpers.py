def is_sorted(lst):
    return all(a <= b for a, b in zip(lst, lst[1:]))


def next_smaller(lst):
    last_item = None
    i = 0
    for index, item in enumerate(lst):
        if item == 0:
            break
        if last_item is None or (item >= last_item and index == i):
            last_item = item
            i += 1
            yield item


def valid_pka_values(values):
    values = list(values)
    result = []
    if values[0] == 0:
        pass
    elif is_sorted(values):
        result = values
    else:
        result = list(next_smaller(values))
    return result
