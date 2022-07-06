import pytest
from tax_calculator import calculate_tax_reduction


@pytest.mark.parametrize(
    'tax, expected',
    [
        (-5000, 0),
        (0, 0),
        (5000, 0),
        (10000, 0),
        (15000, 5000)
    ]
)
def test_calculate_tax_reduction(tax, expected):
    actual = calculate_tax_reduction(tax)
    assert actual == expected
