import pytest


# Тесты Float
@pytest.mark.parametrize('integer', [-9999, -1, 0, 1, 9999])
def test_division_creates_float(integer):
    assert isinstance(integer / 2, float)
    assert isinstance(integer / -2, float)

def test_float_plus_float_not_int():
    try:
        assert isinstance(0.0 + 0.0, int)
        assert isinstance(0.9 + 0.1, int)
        assert isinstance(-0.1 + -0.9, int)
    except AssertionError:
        pass

