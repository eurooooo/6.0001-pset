# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 17:49:31 2021

@author: 52900
"""

annual_salary=int(input('Enter your annual salary:'))
portion_saved=float(input('Enter the percent of your salary to save, as a decimal:'))
total_cost=int(input('Enter the cost of your dream home: '))
semi_annual_raise=float(input('Enter the semi­annual raise, as a decimal:'))
portion_down_payment=0.25
current_savings=0.0
monthly_salary=annual_salary/12
r=0.04
Number_of_months=0
while current_savings < total_cost*portion_down_payment:
    if  Number_of_months%6==0 and Number_of_months>0:
        monthly_salary+=monthly_salary*semi_annual_raise
    current_savings+=current_savings*r/12+monthly_salary*portion_saved
    Number_of_months+=1
print('Number of months:',Number_of_months)