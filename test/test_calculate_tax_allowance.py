from tax_calculator import calculate_tax_allowance
from conftest import fixture_allowance


def test_calculate_tax_allowance_negative_allowance_1(fixture_allowance):
    actual = calculate_tax_allowance(-1, fixture_allowance[0])
    expected = 0
    assert actual == expected


def test_calculate_tax_allowance_negative_allowance_2(fixture_allowance):
    actual = calculate_tax_allowance(0, fixture_allowance[0])
    expected = 0
    assert actual == expected


def test_calculate_tax_allowance_negative_allowance_3(fixture_allowance):
    actual = calculate_tax_allowance(132000, fixture_allowance[0])
    expected = 0
    assert actual == expected


def test_calculate_tax_allowance_negative_allowance_4(fixture_allowance):
    actual = calculate_tax_allowance(132001, fixture_allowance[0])
    expected = 1
    assert actual == expected


def test_calculate_tax_allowance_zero_allowance_1(fixture_allowance):
    actual = calculate_tax_allowance(-1, fixture_allowance[1])
    expected = 0
    assert actual == expected


def test_calculate_tax_allowance_zero_allowance_2(fixture_allowance):
    actual = calculate_tax_allowance(0, fixture_allowance[1])
    expected = 0
    assert actual == expected


def test_calculate_tax_allowance_zero_allowance_3(fixture_allowance):
    actual = calculate_tax_allowance(1, fixture_allowance[1])
    expected = 0
    assert actual == expected


def test_calculate_tax_allowance_zero_allowance_4(fixture_allowance):
    actual = calculate_tax_allowance(132000, fixture_allowance[1])
    expected = 0
    assert actual == expected


def test_calculate_tax_allowance_zero_allowance_5(fixture_allowance):
    actual = calculate_tax_allowance(132001, fixture_allowance[1])
    expected = 1
    assert actual == expected


def test_calculate_tax_allowance_normal_allowance1_1(fixture_allowance):
    actual = calculate_tax_allowance(-1, fixture_allowance[2])
    expected = 0
    assert actual == expected


def test_calculate_tax_allowance_normal_allowance1_2(fixture_allowance):
    actual = calculate_tax_allowance(0, fixture_allowance[2])
    expected = 0
    assert actual == expected


def test_calculate_tax_allowance_normal_allowance1_3(fixture_allowance):
    actual = calculate_tax_allowance(1, fixture_allowance[2])
    expected = 0
    assert actual == expected


def test_calculate_tax_allowance_normal_allowance1_4(fixture_allowance):
    actual = calculate_tax_allowance(704500, fixture_allowance[2])
    expected = 0
    assert actual == expected


def test_calculate_tax_allowance_normal_allowance1_5(fixture_allowance):
    actual = calculate_tax_allowance(704501, fixture_allowance[2])
    expected = 1
    assert actual == expected


def test_calculate_tax_allowance_normal_allowance2_1(fixture_allowance):
    actual = calculate_tax_allowance(-1, fixture_allowance[3])
    expected = 0
    assert actual == expected


def test_calculate_tax_allowance_normal_allowance2_2(fixture_allowance):
    actual = calculate_tax_allowance(0, fixture_allowance[3])
    expected = 0
    assert actual == expected


def test_calculate_tax_allowance_normal_allowance2_3(fixture_allowance):
    actual = calculate_tax_allowance(1, fixture_allowance[3])
    expected = 0
    assert actual == expected


def test_calculate_tax_allowance_normal_allowance2_4(fixture_allowance):
    actual = calculate_tax_allowance(704000, fixture_allowance[3])
    expected = 0
    assert actual == expected


def test_calculate_tax_allowance_normal_allowance2_5(fixture_allowance):
    actual = calculate_tax_allowance(704001, fixture_allowance[3])
    expected = 1
    assert actual == expected


def test_calculate_tax_allowance_limit_allowance1_1(fixture_allowance):
    actual = calculate_tax_allowance(-1, fixture_allowance[4])
    expected = 0
    assert actual == expected


def test_calculate_tax_allowance_limit_allowance1_2(fixture_allowance):
    actual = calculate_tax_allowance(0, fixture_allowance[4])
    expected = 0
    assert actual == expected


def test_calculate_tax_allowance_limit_allowance1_3(fixture_allowance):
    actual = calculate_tax_allowance(1, fixture_allowance[4])
    expected = 0
    assert actual == expected


def test_calculate_tax_allowance_limit_allowance1_4(fixture_allowance):
    actual = calculate_tax_allowance(1412000, fixture_allowance[4])
    expected = 0
    assert actual == expected


def test_calculate_tax_allowance_limit_allowance1_5(fixture_allowance):
    actual = calculate_tax_allowance(1412001, fixture_allowance[4])
    expected = 1
    assert actual == expected


def test_calculate_tax_allowance_limit_allowance2_1(fixture_allowance):
    actual = calculate_tax_allowance(-1, fixture_allowance[5])
    expected = 0
    assert actual == expected


def test_calculate_tax_allowance_limit_allowance2_2(fixture_allowance):
    actual = calculate_tax_allowance(0, fixture_allowance[5])
    expected = 0
    assert actual == expected


def test_calculate_tax_allowance_limit_allowance2_3(fixture_allowance):
    actual = calculate_tax_allowance(1, fixture_allowance[5])
    expected = 0
    assert actual == expected


def test_calculate_tax_allowance_limit_allowance2_4(fixture_allowance):
    actual = calculate_tax_allowance(2467000, fixture_allowance[5])
    expected = 0
    assert actual == expected


def test_calculate_tax_allowance_limit_allowance2_5(fixture_allowance):
    actual = calculate_tax_allowance(2467001, fixture_allowance[5])
    expected = 1
    assert actual == expected