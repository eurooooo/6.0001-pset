# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 13:47:22 2021

@author: 52900
"""
annual_salary=int(input('Enter the starting salary: '))
monthly_salary=annual_salary/12
a=monthly_salary
total_cost=1000000
semi_annual_raise=0.07
portion_down_payment=0.25
current_savings=0
r=0.04
Number_of_months=0
high=10000
low=0
Steps_in_bisection_search=0
while current_savings < total_cost*portion_down_payment:
        if  Number_of_months%6==0 and Number_of_months>0:
            monthly_salary+=monthly_salary*semi_annual_raise
        current_savings+=current_savings*r/12+monthly_salary
        Number_of_months+=1
if Number_of_months>36:
    print('It is not possible to pay the down payment in three years.')
else:
    while high-low>0.1:
        monthly_salary=annual_salary/12
        current_savings=0
        Number_of_months=0
        while current_savings < total_cost*portion_down_payment:
            if  Number_of_months%6==0 and Number_of_months>0:
                monthly_salary+=monthly_salary*semi_annual_raise
            current_savings+=current_savings*r/12+monthly_salary*(low+high)/20000
            Number_of_months+=1
        if Number_of_months>36:
            low=(low+high)/2
        else:
            high=(low+high)/2
        Steps_in_bisection_search+=1
    print('Best savings rate: ',(high//1)/10000)
    print('Steps in bisection search:',Steps_in_bisection_search)