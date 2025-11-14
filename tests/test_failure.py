from app.math_utils import sum_numbers


def test_sum_numbers_success():
    assert sum_numbers(2, 3) == 5


def test_sum_numbers_fail():
    assert sum_numbers(1, 1) == 3
