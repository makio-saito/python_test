from src.myfunc import add, sub


def test_add():
    assert add(1, 2) == 3


def test_sub():
    assert sub(2, 1) == 2


class TestCase:
    def test_true(self):
        assert True

    def test_add_zero(self):
        assert add(1, 0) == 0

    def test_sub_zero(self):
        assert sub(1, 0) == 1
