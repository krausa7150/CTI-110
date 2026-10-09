# Alex Kraus
# CTI 110
# 10/08/26
# P3HW2

"""
PSEUDOCODE:
Ask for employee name
Ask for hours worked
Ask for pay rate

If hours worked > 40:
    overtime hours = hours worked - 40
    overtime pay = overtime hours * (pay rate * 1.5)
    regular pay = 40 * pay rate
Else:
    overtime hours = 0
    overtime pay = 0
    regular pay = hours worked * pay rate

gross pay = regular pay + overtime pay

Print all results
"""

# INPUT
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# CALCULATIONS
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_pay = 40 * pay_rate
else:
    overtime_hours = 0
    overtime_pay = 0
    regular_pay = hours_worked * pay_rate

gross_pay = regular_pay + overtime_pay

# OUTPUT
print("--------------------------------------------------")
print("Employee Name:", employee_name)
print("Hours Worked:", hours_worked)
print("Pay Rate:", pay_rate)
print("Overtime Hours:", overtime_hours)
print("Overtime Pay:", overtime_pay)
print("Regular Pay:", regular_pay)
print("Gross Pay:", gross_pay)
print("--------------------------------------------------")