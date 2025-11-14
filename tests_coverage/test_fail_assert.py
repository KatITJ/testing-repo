# test_fail_assert.py
def test_sum_fail():
    result = 1 + 1
    assert result == 3, "Expected 1+1 to equal 3 (intentional fail)"
