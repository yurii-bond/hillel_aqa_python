import lecture_11.tdd.calculator as calc


def test_add_two_values():
    assert calc.add(2, 2) == 4


def test_add_two_negative_values():
    assert calc.add(-2, -2) == -4


def test_add_two_str_values():
    assert calc.add('2', '2') == '22'

