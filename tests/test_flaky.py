import random


def test_flaky():
    # 20% chance of passing
    assert random.randint(1, 5) == 1
