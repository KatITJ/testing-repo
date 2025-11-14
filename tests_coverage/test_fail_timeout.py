# test_fail_timeout.py
import time


def test_slow_test():
    time.sleep(2)  # Simulate slow test
    assert False, "Intentional slow failure"
