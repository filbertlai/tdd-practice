def check_and_correct_for_limit(dictionary: dict, key: str, limit: int) -> dict:
    """
    This function checks the dictionary to see if the value is exceeding the limitation.
    If so, this function will change the value to the highest/lowest possible value.

    :param dictionary: dictionary for checking
    :param key: key name for checking
    :param limit: limitation for that item
    :return: dictionary changed to meet the limitation
    """
    if dictionary[key] > limit:
        dictionary[key] = limit
    elif dictionary[key] < 0:
        dictionary[key] = 0
    return dictionary


def calculate_tax_allowance(income: float, allowances: dict) -> float:
    """
    This function calculates the intermediate result for the tax allowance part.

    :param income: income for the year of assessment
    :param allowances: conditions for calculating tax allowance, e.g. number of child
    :return: intermediate result that have calculated for the tax allowance
    """
    # Value checking
    if income <= 0:
        return 0

    tax = income

    # Basic allowance
    tax -= 132000

    # Other years child allowance
    allowances = check_and_correct_for_limit(allowances, 'number of other years child', 9)
    allowances = check_and_correct_for_limit(allowances, 'number of current years child', 9)
    tax -= 120000 * (allowances['number of other years child'] + allowances['number of current years child'])

    # Current years child allowance
    tax -= 120000 * allowances['number of current years child']

    # Dependent brother and sister allowance
    allowances = check_and_correct_for_limit(allowances, 'number of dependent brother and sister', 9)
    tax -= 37500 * allowances['number of dependent brother and sister']

    # Dependent parent allowances (55-60)
    allowances = check_and_correct_for_limit(allowances, 'number of dependent parent (55-60) - resided', 4)
    allowances = check_and_correct_for_limit(allowances, 'number of dependent parent (55-60) - not resided', 4)
    tax -= 25000 * allowances['number of dependent parent (55-60) - resided'] * 2
    tax -= 25000 * allowances['number of dependent parent (55-60) - not resided']

    # Dependent parent allowances (>=60 or under 60 disability)
    allowances = check_and_correct_for_limit(allowances,
                                             'number of dependent parent (>=60 or under 60 disability) - resided', 4)
    allowances = check_and_correct_for_limit(allowances,
                                             'number of dependent parent (>=60 or under 60 disability) - not resided',
                                             4)
    tax -= 50000 * allowances['number of dependent parent (>=60 or under 60 disability) - resided'] * 2
    tax -= 50000 * allowances['number of dependent parent (>=60 or under 60 disability) - not resided']

    # Single parent allowance
    if allowances['single parent']:
        tax -= 132000

    # Disabled dependant allowance
    if allowances['number of disabled dependant'] < 0:
        allowances['number of disabled dependant'] = 0
    tax -= 75000 * allowances['number of disabled dependant']

    # Personal disability allowance
    if allowances['personal disability']:
        tax -= 75000

    if tax < 0:
        return 0
    return tax


def calculate_tax_deduction(tax: float, expenses: dict) -> float:
    """
    This function calculates the intermediate result after tax deduction.

    :param tax: intermediate result from the last part (tax allowance)
    :param expenses: expenses for calculating tax deduction, e.g. expenses for self-education
    :return: intermediate result that have calculated for the tax deduction
    """
    # Value checking
    if tax <= 0:
        return 0

    # Upper limit of expenses
    limits = {
        'Expense of self-education': 100000,
        'Elderly Residential Card Expense': 100000,
        'Home Loan Interest': 100000,
        'Mandatory Contributions to Recognized Retirement Schemes': 18000,
        'Qualifying Premiums Paid under Voluntary Health Insurance Scheme': 8000,
        'Qualifying Annuity Premiums and Tax Deductible MPF Voluntary Contributions': 60000,
        'Domestic Rent Deduction': 100000
    }

    for key in limits:
        limit = limits[key]
        expense = expenses[key]

        if expense < 0:
            expense = 0
        if expense > limit:
            tax -= limit
        else:
            tax -= expense

    if tax < 0:
        tax = 0
    return tax


def calculate_salary_tax_after_allowance(net_chargeable_income: float) -> float:
    """
    This function calculates the intermediate result after tax deduction.

    :param net_chargeable_income: net chargeable income, which is equals to income - tax reduction
    :return: intermediate result that have calculated for the rates
    """
    # Value checking
    if net_chargeable_income <= 0:
        return 0

    rates = [0.02, 0.06, 0.1, 0.14, 0.17]
    tax = 0
    remain = net_chargeable_income
    level = 0
    while remain > 0:
        rate = rates[level]
        if remain <= 50000 or rate == rates[-1]:
            tax += remain * rate
            break
        else:
            tax += 50000 * rate
            remain -= 50000
            level += 1
    return tax


def calculate_tax_reduction(tax: float) -> float:
    """
    This function calculates the final result after tax reduction
    :param tax: intermediate result passed from the last part
    :return: final result
    """
    # Value checking
    if tax <= 0:
        return 0

    result = tax - 10000
    if result < 0:
        return 0
    return result


class tax_calculator:
    income = 0
    allowance = {
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
    expenses = {
        'Expense of self-education': 0,
        'Elderly Residential Card Expense': 0,
        'Home Loan Interest': 0,
        'Mandatory Contributions to Recognized Retirement Schemes': 0,
        'Qualifying Premiums Paid under Voluntary Health Insurance Scheme': 0,
        'Qualifying Annuity Premiums and Tax Deductible MPF Voluntary Contributions': 0,
        'Domestic Rent Deduction': 0
    }

    def __init__(self, income, allowance, expenses):
        self.income = income
        if allowance is not None: self.allowance = allowance
        if expenses is not None: self.expenses = expenses

    def calculate(self):
        tax = calculate_tax_allowance(self.income, self.allowance)
        tax = calculate_tax_deduction(tax, self.expenses)
        tax = calculate_salary_tax_after_allowance(tax)
        tax = calculate_tax_reduction(tax)
        return tax