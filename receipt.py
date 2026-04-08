
price = float(input("Type products price: "))
qua = int(input("Type Quantity: "))
print("Are you a member ?")
member = bool(input("1 for yes \nnothing for no\n"))
sum = price * qua;
if member : 
    
    sum -= (price*qua)*(10/100) ;


vat = (sum) * (24/100);
total = sum + vat;

print("\n_____ JOHNS Grocery store _____")
print(f"|Your total is: {sum}           |")
print(f"|Your products VAT is: {vat:.2f}    |")
print(f"|Your total with vat is: {total:.2f} |")
print("|______________________________|")