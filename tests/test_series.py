from series import __version__
from series.series import fibonacci, lucas, sum_series
def test_version():
    assert __version__ == '0.1.0'


def test_one():
    expected = 3
    actual = fibonacci(4)
    assert actual == expected
def test_two():
    expected = 13
    actual = fibonacci(7)
    assert actual == expected

def test_three():
    expected = 144
    actual = fibonacci(12)
    assert actual == expected

def test_four():
    expected = 29
    actual = lucas(7)
    assert actual == expected

def test_five():
    expected = 123
    actual = lucas(10)
    assert actual == expected

def test_six():
    expected = 3
    actual = sum_series(4)
    assert actual == expected

def test_seven():
    expected = 322
    actual = sum_series(12, 2, 1)
    assert actual == expected

def test_eight():
    expected = 75025
    actual = sum_series(25)
    assert actual == expected

def test_nine():
    expected = 178
    actual = sum_series(8, 4, 6)
    assert actual == expected

def test_ten():
    expected = 257
    actual = sum_series(6, 13, 24)
    assert actual == expected

def test_eleven():
    expected = 15737
    actual = sum_series(17, 3, 8)
    assert actual == expected

def test_twelve():
    expected = 11
    actual = lucas(5)
    assert actual == expected