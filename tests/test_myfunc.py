from src.myfunc import add, sub


def test_add():
    assert add(1, 2) == 3


def test_sub():
    assert sub(2, 1) == 0
