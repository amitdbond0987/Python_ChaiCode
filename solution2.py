age=int(input("Enter your age : "))
day=input("Enter day : ")
low=day.lower()

price = 12 if age>18 else 8

if low == "wednesday":
    if age > 18:
        price = price-2
    else:
        price = price-2
else:
    if age>18:
        price = 12
    else:
        price = 8

print(price)
