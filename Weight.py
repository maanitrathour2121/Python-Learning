weight = int(input("Please enter your weight: "))
pounds_or_kg = input("(L)bs or (K)g: ")
if pounds_or_kg.upper() == "L":
    converted = weight // 2.205
    print(f"You are {converted} kilos !")
elif pounds_or_kg.upper() == "K":
    converted = weight * 2.205
    print(f"You are {converted} pounds !")
else:
    print("Please enter a valid weight unit!")