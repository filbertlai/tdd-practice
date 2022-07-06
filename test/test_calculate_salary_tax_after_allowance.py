import pytest
from tax_calculator import calculate_salary_tax_after_allowance


@pytest.mark.parametrize(
    'income, expected',
    [
        (-25000, 0),
        (0, 0),
        (25000, 500),
        (50000, 1000),
        (75000, 2500),
        (100000, 4000),
        (125000, 6500),
        (150000, 9000),
        (175000, 12500),
        (200000, 16000),
        (250000, 24500),
    ]
)
def test_calculate_tax_reduction(income, expected):
    actual = calculate_salary_tax_after_allowance(income)
    assert actual == expected
