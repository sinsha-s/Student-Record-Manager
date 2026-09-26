print("=== Student Record Manager ===")

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

python_mark = int(input("Enter Python mark: "))
maths_mark = int(input("Enter Maths mark: "))
english_mark = int(input("Enter English mark: "))

total = python_mark + maths_mark + english_mark
percentage = total / 3

if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "F"

if percentage >= 40:
    result = "Pass"
else:
    result = "Fail"

attendance = int(input("Enter attendance percentage: "))

if attendance >= 75:
    attendance_status = "Eligible"
else:
    attendance_status = "Not Eligible"

print("\n===== STUDENT REPORT =====")
print("Name:", name)
print("Roll Number:", roll_no)
print("Total:", total)
print("Percentage:", percentage)
print("Grade:", grade)
print("Result:", result)
print("Attendance:", attendance)
print("Attendance Status:", attendance_status)