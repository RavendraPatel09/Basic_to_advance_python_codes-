marks = []
n = int(input("Enter number of subjects: "))

for i in range(n):
    m = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(m)

total = sum(marks)
percentage = total / n

if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "Fail"

print("Total:", total)
print("Percentage:", percentage)
print("Grade:", grade)