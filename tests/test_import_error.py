import non_existent_module  # <-- pytest lo mete en collectors como failure


def test_should_never_run():
    assert True
