marks1 = int(input("Enter marks for subject 1: "))
if marks1 < 0 or marks1 > 100:
    print("Invalid marks entered. Please enter marks between 0 and 100.")
    exit()
marks2 = int(input("Enter marks for subject 2: "))
if marks2 < 0 or marks2 > 100:
    print("Invalid marks entered. Please enter marks between 0 and 100.")
    exit()
marks3 = int(input("Enter marks for subject 3: "))
if marks3 < 0 or marks3 > 100:
    print("Invalid marks entered. Please enter marks between 0 and 100.")
    exit()

total_marks = marks1 + marks2 + marks3
total_percentage = round((total_marks / 300) * 100, 2)

indiv_percentage1 = round((marks1 / 100) * 100, 2)
indiv_percentage2 = round((marks2 / 100) * 100, 2)
indiv_percentage3 = round((marks3 / 100) * 100, 2)

if total_percentage >= 90:
    print("WOW ! You have scored A+ grade.", total_percentage)

elif total_percentage >= 40 and indiv_percentage1 >= 33 and indiv_percentage2 >= 33 and indiv_percentage3 >= 33:
    print("You have passed the exam.", total_percentage)
else:
    print("You have failed the exam.", total_percentage)

