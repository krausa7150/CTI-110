# Alex Kraus
# 10/21/26
# CTI 110
# Updated Grade Scores

# Ask user for number of scores
num_scores = int(input("How many scores do you want to enter? "))

# Create empty score list
grade_list = []

# Collect scores
for score_num in range(1, num_scores + 1):

    score = float(input(f"Enter score #{score_num}: "))

    while score < 0 or score > 100:
        print()
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{score_num} again: "))

    grade_list.append(score)

# Find lowest grade
lowest_grade = min(grade_list)

# Remove lowest grade
grade_list.remove(lowest_grade)

# Calculate average
average = sum(grade_list) / len(grade_list)

# Determine letter grade
if average >= 90:
    letter_grade = "A"
elif average >= 80:
    letter_grade = "B"
elif average >= 70:
    letter_grade = "C"
elif average >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Display results
print("\n------------Results------------")
print("Lowest Score  :", lowest_grade)
print("Modified List :", grade_list)
print("Scores Average:", format(average, ".2f"))
print("Grade         :", letter_grade)
print("--------------------------------")