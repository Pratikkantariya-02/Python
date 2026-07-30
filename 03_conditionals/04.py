fruit = str(input("Enter fruit name : "))
color = str(input("Enter color name : "))

if fruit == "Banana":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("OverRipe")