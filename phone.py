pagio=float(input("Dose pagio"))
lepta=float(input("Dose lepta"))
dlepta=float(input("Dose dlepta"))
total = 0
extra = 0 
if lepta<=dlepta :
    total += pagio
    print(f"Your total without vat is {total}")
elif lepta>dlepta :
    extra =int(lepta - dlepta ) 
    for i in range(extra):
        total += 0.10
    total += pagio
    print(f"Your total  without vat is {total}")

if total > 50 :
    print("too expensive this month ")

total += total * 0.24
print(f"your total with vat is {total:.2f}")




