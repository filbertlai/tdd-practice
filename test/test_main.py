from tax_calculator import tax_calculator
from conftest import fixture_main


def test_calculate_main_1(fixture_main):
    fixture = fixture_main[0]
    actual = tax_calculator(fixture[0], fixture[1], fixture[2]).calculate()
    expected = 149735
    assert actual == expected


def test_calculate_main_2(fixture_main):
    fixture = fixture_main[1]
    actual = tax_calculator(fixture[0], fixture[1], fixture[2]).calculate()
    expected = 716260
    assert actual == expected


def test_calculate_main_3(mocker, fixture_main):
    mocker.patch("tax_calculator.calculate_tax_deduction", return_value=0)
    fixture = fixture_main[1]
    actual = tax_calculator(fixture[0], fixture[1], fixture[2]).calculate()
    expected = 0
    assert actual == expected