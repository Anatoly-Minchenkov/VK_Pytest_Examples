import pytest


# Float Tests
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


# List Tests
@pytest.mark.parametrize('test_list', [[12, 13, 14], [], [999]])
def test_lists_are_mutable(test_list):
    test_list.append(12)
    assert test_list[-1] == 12
    test_list[0] = 'Hello'
    assert test_list[0] == 'Hello'


def test_out_of_range_list():
    try:
        test_list = []
        assert test_list[0]
        test_list = [1, 2, 3, 4, 5]
        assert test_list[7]
        assert test_list[70]
        assert test_list[-7]
    except IndexError:
        pass


# Tuple Tests

@pytest.mark.parametrize('test_tuple, result', [((1,), (1, 1, 1)), ((), ()), ((12, 13), (12, 13, 12, 13, 12, 13))])
def test_tuple_can_multiply(test_tuple, result):
    assert test_tuple * 3 == result


def test_tuple_are_immutable():
    try:
        test_tuple = (5, 4, 3, 2, 1)
        assert test_tuple.append(10)
        assert test_tuple.remove(1)
        assert test_tuple.pop(2)
        assert test_tuple.sort()
    except AttributeError:
        pass
