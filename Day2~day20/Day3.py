print("Welcome Pizza")
print(10%3)
# height = int(input("Write ur height"))
# if height <= 120:
#     print("ur not allowed")
# else:
#     print("ur ok")
price = 0
size = input("size?")
pepperoni = input("pepp? Y or N")
cheese = input("cheese Y or N")

if size == "M":
    price = 20
elif size == "S":
    price = 15
elif size == "L":
    price = 25
else:
    print("no")
if pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price += 3
if cheese == "Y":
    price += 1
print(f"price is: ${price}.")

 