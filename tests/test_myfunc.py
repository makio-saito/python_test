from src.myfunc import add, sub


def test_add():
    import json
    import os
    with open('environ.json', 'w') as f:
        json.dump()
        json.dump(dict(os.environ), f, indent=4)

    assert add(1, 2) == 3


def test_sub():
    assert sub(2, 1) == 1


class TestCase:
    def test_true(self):
        assert True

    def test_add_zero(self):
        assert add(1, 0) == 1

    def test_sub_zero(self):
        assert sub(1, 0) == 1
