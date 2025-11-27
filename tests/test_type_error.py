def test_type_error_failure():
    # This will cause a TypeError because you can't add an int to a string
    value = 5 + "text"
    assert value == "should fail"
