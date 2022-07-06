## test_calculate_salary_tax_after_allowance.py
I have used parametrize to test the function calculate_salary_tax_after_allowance. There are 11 different incomes were tested, ranging from -25000 to 250000, which was incremented for 25,000 for each row.

## test_calculate_tax_allowance.py
I have used fixture to test the function calculate_tax_allowance. There are 29 test cases in total. I have written 6 different conditions for calculating tax allowance in conftest.py. For each condition, I have tested another input which is the intermediate tax result with value in negative, zero, small positive, normal positive and outside limitations.

## test_calculate_tax_deduction.py
I have used fixture to test the function calculate_tax_deduction. There are 18 test cases in total. I have written 5 different conditions for calculating tax reduction in conftest.py. For each condition, I have tested another input which is the intermediate tax result with value in negative, zero, small positive, normal positive and outside limitations.

## test_main.py
I have used fixture and mocker to test the entire flow in tax_calculator.py. Since the edge cases were tested in other programs already, I have not tested for the edge cases in this file. Instead, I have tested for 3 test cases with normal input in total, which comes from 2 fixture cases in conftest.py. I have randomly selected some value in the conditions for calculating the allowance and reduction respectively. I have verified the result from my program with the online calculator already. All results are the same (except that the online calculator will not reduce 10,000 at the end of the calculation).

## test_tax_calculator_reduction.py
I have used parametrize to test the function tax_calculator_reduction. There are 5 different input were tested, ranging from -5000 to 15000, which was incremented for 5000 for each row.