from src.helpers import valid_pka_values


def test_three_zero_inputs_three_pka():
    assert valid_pka_values((0, 0, 0)) == [0, 0, 0]


def test_three_inputs_one_pka():
    assert valid_pka_values((1, 0, 0)) == [1]


def test_three_inputs_two_pkas():
    assert valid_pka_values((1, 1, 0)) == [1, 1]


def test_three_inputs_two_pkas_alternate():
    assert valid_pka_values((1, 0, 1)) == [1]


def test_three_inputs_equal():
    assert valid_pka_values((1, 1, 1)) == [1, 1, 1]


def test_four_zero_inputs_four_pka():
    assert valid_pka_values((0, 0, 0, 0)) == [0, 0, 0, 0]


def test_three_inputs_sorted():
    assert valid_pka_values((1, 2, 3)) == [1, 2, 3]


def test_three_inputs_sorted_first_zero():
    assert valid_pka_values((0, 2, 3)) == [0, 2, 3]


def test_three_inputs_sorted_two_equal():
    assert valid_pka_values((1, 2, 2)) == [1, 2, 2]


def test_three_inputs_sorted_two_valid():
    assert valid_pka_values((1, 2, 1)) == [1, 2]


def test_four_inputs_sorted_two_valid():
    assert valid_pka_values((1, 2, 1, 3)) == [1, 2]


def test_four_inputs_sorted_three_equal_all_valid():
    assert valid_pka_values((1, 1, 1, 3)) == [1, 1, 1, 3]
