from tax_calculator import calculate_tax_deduction
from conftest import fixture_expense


def test_calculate_tax_reduction_negative_expense_1(fixture_expense):
    actual = calculate_tax_deduction(-1, fixture_expense[0])
    expected = 0
    assert actual == expected


def test_calculate_tax_reduction_negative_expense_2(fixture_expense):
    actual = calculate_tax_deduction(0, fixture_expense[0])
    expected = 0
    assert actual == expected


def test_calculate_tax_reduction_negative_expense_3(fixture_expense):
    actual = calculate_tax_deduction(1, fixture_expense[0])
    expected = 1
    assert actual == expected


def test_calculate_tax_reduction_zero_expense_1(fixture_expense):
    actual = calculate_tax_deduction(-1, fixture_expense[1])
    expected = 0
    assert actual == expected


def test_calculate_tax_reduction_zero_expense_2(fixture_expense):
    actual = calculate_tax_deduction(0, fixture_expense[1])
    expected = 0
    assert actual == expected


def test_calculate_tax_reduction_zero_expense_3(fixture_expense):
    actual = calculate_tax_deduction(1, fixture_expense[1])
    expected = 1
    assert actual == expected


def test_calculate_tax_reduction_normal_expense_1(fixture_expense):
    actual = calculate_tax_deduction(-1, fixture_expense[2])
    expected = 0
    assert actual == expected


def test_calculate_tax_reduction_normal_expense_2(fixture_expense):
    actual = calculate_tax_deduction(0, fixture_expense[2])
    expected = 0
    assert actual == expected


def test_calculate_tax_reduction_normal_expense_3(fixture_expense):
    actual = calculate_tax_deduction(1, fixture_expense[2])
    expected = 0
    assert actual == expected


def test_calculate_tax_reduction_normal_expense_4(fixture_expense):
    actual = calculate_tax_deduction(1000000, fixture_expense[2])
    expected = 993000
    assert actual == expected


def test_calculate_tax_reduction_limit_expense_1(fixture_expense):
    actual = calculate_tax_deduction(-1, fixture_expense[3])
    expected = 0
    assert actual == expected


def test_calculate_tax_reduction_limit_expense_2(fixture_expense):
    actual = calculate_tax_deduction(0, fixture_expense[3])
    expected = 0
    assert actual == expected


def test_calculate_tax_reduction_limit_expense_3(fixture_expense):
    actual = calculate_tax_deduction(1, fixture_expense[3])
    expected = 0
    assert actual == expected


def test_calculate_tax_reduction_limit_expense_4(fixture_expense):
    actual = calculate_tax_deduction(1000000, fixture_expense[3])
    expected = 514000
    assert actual == expected


def test_calculate_tax_reduction_greater_expense_1(fixture_expense):
    actual = calculate_tax_deduction(-1, fixture_expense[4])
    expected = 0
    assert actual == expected


def test_calculate_tax_reduction_greater_expense_2(fixture_expense):
    actual = calculate_tax_deduction(0, fixture_expense[4])
    expected = 0
    assert actual == expected


def test_calculate_tax_reduction_greater_expense_3(fixture_expense):
    actual = calculate_tax_deduction(1, fixture_expense[4])
    expected = 0
    assert actual == expected


def test_calculate_tax_reduction_greater_expense_4(fixture_expense):
    actual = calculate_tax_deduction(1000000, fixture_expense[4])
    expected = 514000
    assert actual == expected
