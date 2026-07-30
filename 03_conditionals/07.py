order_size = str(input("Enter order size : "))
extra_shot = input("Please choise extra shot or not : ").lower()

if extra_shot == "yes":
    coffee = order_size + " coffee with extra shot"
else:
    coffee = order_size + " coffee"

print(coffee)