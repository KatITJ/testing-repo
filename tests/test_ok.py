from app.calculator import add, divide


def test_add():
    result = add(1, 2)
    assert result == 3


def test_divide():
    result = divide(10, 2)
    assert result == 5
