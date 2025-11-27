import random
import time


# Simulate a flaky network call with aggressive failure rate
def aggressive_network_call():
    time.sleep(random.uniform(0.005, 0.02))

    # 80% fail test
    if random.random() < 0.8:
        raise ConnectionError("Network disconnect")


def test_network_aggressive():
    aggressive_network_call()
