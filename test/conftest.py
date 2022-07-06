import pytest


@pytest.fixture(autouse=True)
def fixture_expense():
    negative_expense = {
        'Expense of self-education': -1,
        'Elderly Residential Card Expense': -1,
        'Home Loan Interest': -1,
        'Mandatory Contributions to Recognized Retirement Schemes': -1,
        'Qualifying Premiums Paid under Voluntary Health Insurance Scheme': -1,
        'Qualifying Annuity Premiums and Tax Deductible MPF Voluntary Contributions': -1,
        'Domestic Rent Deduction': -1,
    }

    zero_expense = {
        'Expense of self-education': 0,
        'Elderly Residential Card Expense': 0,
        'Home Loan Interest': 0,
        'Mandatory Contributions to Recognized Retirement Schemes': 0,
        'Qualifying Premiums Paid under Voluntary Health Insurance Scheme': 0,
        'Qualifying Annuity Premiums and Tax Deductible MPF Voluntary Contributions': 0,
        'Domestic Rent Deduction': 0,
    }

    normal_expense = {
        'Expense of self-education': 1000,
        'Elderly Residential Card Expense': 1000,
        'Home Loan Interest': 1000,
        'Mandatory Contributions to Recognized Retirement Schemes': 1000,
        'Qualifying Premiums Paid under Voluntary Health Insurance Scheme': 1000,
        'Qualifying Annuity Premiums and Tax Deductible MPF Voluntary Contributions': 1000,
        'Domestic Rent Deduction': 1000
    }

    limit_expense = {
        'Expense of self-education': 100000,
        'Elderly Residential Card Expense': 100000,
        'Home Loan Interest': 100000,
        'Mandatory Contributions to Recognized Retirement Schemes': 18000,
        'Qualifying Premiums Paid under Voluntary Health Insurance Scheme': 8000,
        'Qualifying Annuity Premiums and Tax Deductible MPF Voluntary Contributions': 60000,
        'Domestic Rent Deduction': 100000
    }

    greater_expense = {
        'Expense of self-education': 200000,
        'Elderly Residential Card Expense': 200000,
        'Home Loan Interest': 200000,
        'Mandatory Contributions to Recognized Retirement Schemes': 200000,
        'Qualifying Premiums Paid under Voluntary Health Insurance Scheme': 200000,
        'Qualifying Annuity Premiums and Tax Deductible MPF Voluntary Contributions': 200000,
        'Domestic Rent Deduction': 200000,
    }

    return [negative_expense, zero_expense, normal_expense, limit_expense, greater_expense]


@pytest.fixture(autouse=True)
def fixture_allowance():
    allowance_negative = {
        'number of other years child': -1,
        'number of current years child': -1,
        'number of dependent brother and sister': -1,
        'number of dependent parent (55-60) - resided': -1,
        'number of dependent parent (55-60) - not resided': -1,
        'number of dependent parent (>=60 or under 60 disability) - resided': -1,
        'number of dependent parent (>=60 or under 60 disability) - not resided': -1,
        'single parent': False,
        'number of disabled dependant': -1,
        'personal disability': False
    }

    allowance_zero = {
        'number of other years child': 0,
        'number of current years child': 0,
        'number of dependent brother and sister': 0,
        'number of dependent parent (55-60) - resided': 0,
        'number of dependent parent (55-60) - not resided': 0,
        'number of dependent parent (>=60 or under 60 disability) - resided': 0,
        'number of dependent parent (>=60 or under 60 disability) - not resided': 0,
        'single parent': False,
        'number of disabled dependant': 0,
        'personal disability': False
    }

    allowance_normal1 = {
        'number of other years child': 1,
        'number of current years child': 1,
        'number of dependent brother and sister': 1,
        'number of dependent parent (55-60) - resided': 1,
        'number of dependent parent (55-60) - not resided': 0,
        'number of dependent parent (>=60 or under 60 disability) - resided': 0,
        'number of dependent parent (>=60 or under 60 disability) - not resided': 1,
        'single parent': False,
        'number of disabled dependant': 1,
        'personal disability': False
    }

    allowance_normal2 = {
        'number of other years child': 2,
        'number of current years child': 0,
        'number of dependent brother and sister': 0,
        'number of dependent parent (55-60) - resided': 0,
        'number of dependent parent (55-60) - not resided': 1,
        'number of dependent parent (>=60 or under 60 disability) - resided': 1,
        'number of dependent parent (>=60 or under 60 disability) - not resided': 0,
        'single parent': True,
        'number of disabled dependant': 0,
        'personal disability': True
    }

    allowance_limit1 = {
        'number of other years child': 100,
        'number of current years child': 0,
        'number of dependent brother and sister': 0,
        'number of dependent parent (55-60) - resided': 1000,
        'number of dependent parent (55-60) - not resided': 0,
        'number of dependent parent (>=60 or under 60 disability) - resided': 0,
        'number of dependent parent (>=60 or under 60 disability) - not resided': 0,
        'single parent': False,
        'number of disabled dependant': 0,
        'personal disability': False
    }

    allowance_limit2 = {
        'number of other years child': 0,
        'number of current years child': 100,
        'number of dependent brother and sister': 0,
        'number of dependent parent (55-60) - resided': 0,
        'number of dependent parent (55-60) - not resided': 1000,
        'number of dependent parent (>=60 or under 60 disability) - resided': 0,
        'number of dependent parent (>=60 or under 60 disability) - not resided': 0,
        'single parent': False,
        'number of disabled dependant': 1,
        'personal disability': False
    }

    return [allowance_negative, allowance_zero, allowance_normal1, allowance_normal2, allowance_limit1, allowance_limit2]


@pytest.fixture(autouse=True)
def fixture_main():
    income1 = 2000000
    allowance1 = {
        'number of other years child': 1,
        'number of current years child': 1,
        'number of dependent brother and sister': 1,
        'number of dependent parent (55-60) - resided': 1,
        'number of dependent parent (55-60) - not resided': 1,
        'number of dependent parent (>=60 or under 60 disability) - resided': 1,
        'number of dependent parent (>=60 or under 60 disability) - not resided': 1,
        'single parent': True,
        'number of disabled dependant': 0,
        'personal disability': False
    }
    expense1 = {
        'Expense of self-education': 10000,
        'Elderly Residential Card Expense': 10000,
        'Home Loan Interest': 10000,
        'Mandatory Contributions to Recognized Retirement Schemes': 10000,
        'Qualifying Premiums Paid under Voluntary Health Insurance Scheme': 8000,
        'Qualifying Annuity Premiums and Tax Deductible MPF Voluntary Contributions': 10000,
        'Domestic Rent Deduction': 10000
    }
    combination1 = [income1, allowance1, expense1]

    income2 = 5000000
    allowance2 = {
        'number of other years child': 2,
        'number of current years child': 0,
        'number of dependent brother and sister': 2,
        'number of dependent parent (55-60) - resided': 1,
        'number of dependent parent (55-60) - not resided': 0,
        'number of dependent parent (>=60 or under 60 disability) - resided': 0,
        'number of dependent parent (>=60 or under 60 disability) - not resided': 1,
        'single parent': False,
        'number of disabled dependant': 0,
        'personal disability': True
    }
    expense2 = {
        'Expense of self-education': 0,
        'Elderly Residential Card Expense': 0,
        'Home Loan Interest': 0,
        'Mandatory Contributions to Recognized Retirement Schemes': 0,
        'Qualifying Premiums Paid under Voluntary Health Insurance Scheme': 0,
        'Qualifying Annuity Premiums and Tax Deductible MPF Voluntary Contributions': 0,
        'Domestic Rent Deduction': 0
    }
    combination2 = [income2, allowance2, expense2]

    return [combination1, combination2]
