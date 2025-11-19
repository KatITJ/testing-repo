import random


def test_flaky():
    # 50% probabilidad de pasar / fallar
    assert random.choice([True, False])
