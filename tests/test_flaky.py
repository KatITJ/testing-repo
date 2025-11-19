import random, time


# This test is intentionally flaky; it will pass approximately 50% of the time.
def test_flaky():
    rnd = int(time.time() * 1_000_000) % 2
    assert rnd == 1
