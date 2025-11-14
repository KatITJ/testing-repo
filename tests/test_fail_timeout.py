import time


def test_slow_test():
    time.sleep(2)
    assert False, "Intentional slow failure"
