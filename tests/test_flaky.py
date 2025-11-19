import random, time


def test_flaky():
    rnd = int(time.time() * 1_000_000) % 2
    assert rnd == 1
