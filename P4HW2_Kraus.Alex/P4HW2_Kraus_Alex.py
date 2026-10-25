# Alex Kraus
# CTI 110
# 10/25/26
# P4HW2
#Pay Calculations for multiple employees and display totals

"""
PSEUDOCODE:

Set total overtime pay to 0
Set total regular pay to 0
Set total gross pay to 0
Set employee count to 0

Ask for employee name

While employee name is not "Done":

    Ask for hours worked
    Ask for pay rate

    If hours worked > 40:
        Calculate overtime hours
        Calculate overtime pay
        Calculate regular pay
    Else:
        Set overtime hours to 0
        Set overtime pay to 0
        Calculate regular pay

    Calculate gross pay

    Add overtime pay to total overtime pay
    Add regular pay to total regular pay
    Add gross pay to total gross pay

    Increase employee count by 1

    Display employee pay information

    Ask for another employee name

Display totals
"""

# Initial totals
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

# First employee name
employee_name = input("Enter employee's name or Done to terminate: ")

# Sentinel loop
while employee_name != "Done":

    hours_worked = float(input("Enter number of hours worked: "))
    pay_rate = float(input("Enter employee's pay rate: "))

    # Calculations
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)
        regular_pay = 40 * pay_rate
    else:
        overtime_hours = 0
        overtime_pay = 0
        regular_pay = hours_worked * pay_rate

    gross_pay = regular_pay + overtime_pay

    # Update totals
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1

    # Employee output
    print("\n--------------------------------------------------")
    print("Employee Name:", employee_name)
    print(f"Hours Worked: {hours_worked:.2f}")
    print(f"Pay Rate: ${pay_rate:.2f}")
    print(f"Overtime Hours: {overtime_hours:.2f}")
    print(f"Overtime Pay: ${overtime_pay:.2f}")
    print(f"Regular Pay: ${regular_pay:.2f}")
    print(f"Gross Pay: ${gross_pay:.2f}")
    print("--------------------------------------------------")

    # Get next employee
    employee_name = input("\nEnter employee's name or Done to terminate: ")

# Final totals
print("\nTotal number of employees entered:", employee_count)
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")