# Alex Kraus
# P3HW1
# CTI 110
# 10/01/26

mod_1 = input("Enter grade for Module 1: ")
mod_2 = input("Enter grade for Module 2: ")
mod_3 = input("Enter grade for Module 3: ")
mod_4 = input("Enter grade for Module 4: ")
mod_5 = input("Enter grade for Module 5: ")
mod_6 = input("Enter grade for Module 6: ")

grades = (mod_1,mod_2,mod_3,mod_4,mod_5,mod_6)

Low = min(grades)
High = max(grades)
total = sum(grades)
avg = total / len(grades)

letter_grade= ""
if avg >= 90:
    letter_grade = "A"
if avg > 80:
     letter_grade = "B"
if avg > 70:
     letter_grade = "C"
if avg > 60:
     letter_grade = "D"
if avg > 50:
     letter_grade = "F"

print("-------RESULTS--------")
print("Lowest grade: ", Low)
print("Highest grade: ", High)
print("Sum of grades: ", total)
print("Average", avg)
print("Your grade is: ", letter_grade)