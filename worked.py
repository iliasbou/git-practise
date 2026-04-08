worked_hours = 0
days=int(input("Type Your worked days "))
for i in range(days):
    hours=float(input(f"Type {i+1} worked hours: "))
    worked_hours+=hours
print(f"Your worked hours of the weekend are {worked_hours}")
