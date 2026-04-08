import statistics
students = []
safe=[]
x = 0
for i in range(8):
    grade=float(input(f"Give the {i} Grade"))
    students.append(grade)

print(f"The average grade is {statistics.mean(students)}")

for student in students:
    if student >= 5 :
        x+=1
        safe.append(student)
print(f"{x} students walked and average is {statistics.mean(safe)}")
