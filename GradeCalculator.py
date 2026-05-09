# grade_calculator.py
marks = [float(input(f"Enter mark {i+1}: ")) for i in range(5)]
avg = sum(marks) / len(marks)

if avg >= 90:
    grade = "A+"
elif avg >= 80:
    grade = "A"
elif avg >= 70:
    grade = "B"
elif avg >= 60:
    grade = "C"
else:
    grade = "F"

print(f"Average: {avg:.2f} | Grade: {grade}")
