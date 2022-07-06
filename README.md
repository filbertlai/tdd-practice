# Test Driven Development Assignment
Instead of the MPF calculator we demonstrated during the class, 
you may also need to create a salary tax calculator to calculate the payable tax amount. 

##Requirement
```
1. Create a tax calculator, you should consider:
    a. Create functions to calculate deduction, you only need to consider the upper limit
    b. Create functions to calculate the allowance, you need to fulfill different condition
        i. resided parent amount will be multiplied by 2
        ii. not resided parent amount will keep in same as table
    c. Assume that the payable tax is only concerned with personal 
    d. All the rules of calculating the payable tax, you should follow the latest definition from IRD 
    
2. It is compulsory to use the features below from pytest:
    a. fixture
    b. parametrize
    c. mocker
3. A coverage report with 100% coverage
4. A document to list out and briefly explain what test cases you have created for this exercise.
```

Here is the table of the salary tax calculation

## Year of Assessment 2018/19 onwards
| | Net chargeable Income | Rate |     
| --- | :-: | :-: |
| | $ | |
| One the First | 50000 | 2% | 
| On the Next | 50000 | 6% |
| On the Next | 50000 | 10% |
| On the Next | 50000 | 14% |
| Remainder | | 17% |
*Net chargeable Income = Income - tax reduction*

## Tax Reduction
| Year of Assessment | % of Tax Reduction | Max Per Case ($)  |
| :-: | :-: | :-: |
| 2021/22 | 100% | 10000 |

## Tax allowance
| Year of Assessment | 2018/19 onwards |  
| :-: | :-: |  
| | $ | |
| Basic allowance | 132,000 |
| Other years child allowance| 120000 |
| Current years child allowance| 120000 |
| Dependent brother and sister allowance| 37500 |
| Dependent parent allowance (55 - 60)| 25000 |
| Dependent parent allowance (>=60 or under 60 disability)| 50000 |
| Single parent allowance | 132000 |
| Disabled dependant allowance | 75000 |
| Personal disability allowance | 75000 |

## Tax deduction
| Year of Assessment | 2018/19 onwards |  
| :-: | :-: |  
| | $ | |
| Expense of self-education | 100000 |
| Elderly Residential Card Expense | 100000 |
| Home Loan Interest | 100000 |
| Mandatory Contributions to Recognized Retirement Schemes| 18000 |
| Qualifying Premiums Paid under Voluntary Health Insurance Scheme| 8000 |
| Qualifying Annuity Premiums and Tax Deductible MPF Voluntary Contributions| 60000 |
| Domestic Rent Deduction | 100000 |
| Approved Charitable Donations | No need to include |



## Tax Allowance and Deduction
You should take reference to [Tax Allowance Table](https://www.ird.gov.hk/chi/pdf/pam61c.pdf)

## Gov Tax calculator
You may go to 
[Tax calculator (EN)](https://www.ird.gov.hk/eng/ese/pa_comp_2022_23_budget/pacfrm.htm)
[Tax calculator (CN)](https://www.ird.gov.hk/chi/ese/st_comp_2020_21/cstcfrm.htm)
to verify your logic

Hand in before Sunday