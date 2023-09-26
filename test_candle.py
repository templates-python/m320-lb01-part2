import pytest

from candle import Candle


@pytest.fixture
def sut():
    return Candle(1, 2)


def test_creation(sut):
    assert True


def test_get_size(sut):
    assert sut.size == 1


def test_invalid_size():
    sut = Candle(-33, 2)
    assert sut.size == -1


def test_get_burning_time(sut):
    assert sut.burning_time == 2


def test_invalid_burning_time():
    sut = Candle(1, -66)
    assert sut.burning_time == -1


def test_burn_does_not_raise_error(sut):
    sut.burn()
