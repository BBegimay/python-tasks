n = int(input("How many tickets?"))
total_price = 0
for i in range(0, n):
    age = int(input("How old is visitor #%d?" % (i + 1)))
    if age < 18:
        price = 0
    elif age < 25:
        price = 990
    else:
        price = 1390
    total_price = price + total_price
if n > 3:
    total_price = total_price * 0.9
print("The total price is", total_price)


