import platform

import pytest


@pytest.mark.skipif(
    platform.system() == 'Linux',
    reason='Because of Linux'
)
@pytest.mark.negative
@pytest.mark.regression
@pytest.mark.sanity
def test_case_example():
    assert 1 + 1 == 2


@pytest.mark.positive
@pytest.mark.regression
@pytest.mark.smoke
def test_smoke_example():
    assert 1 + 1 == 2


@pytest.mark.positive
@pytest.mark.regression
@pytest.mark.smoke
def test_smoke_example2():
    assert 1 + 1 == 2, "Failed due to an error"


@pytest.mark.skip(reason="Причина пропуску тесту")
def test__example():
    assert 1 + 1 == 2


def test_example():
    x = 5
    y = 10
    if x + y != 11:
        pytest.fail("Помилка: Сума x та y не дорівнює 11")


def test_example2():
    x = 5
    y = 10
    if x + y != 11:
        pytest.xfail("Очікуваний результат не співпадає з отриманим")


@pytest.mark.xfail(reason="Reason")
def test_example3():
    x = 5
    y = 10
    assert x + y == 11


def divide(x, y):
    if y == 0:
        raise ValueError("Ділення на нуль неможливе")
    return x / y


def test_divide_by_zero():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert str(exc_info.value) == "Ділення на нуль неможливе"