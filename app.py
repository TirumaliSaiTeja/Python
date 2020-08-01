weight = int(input("weight: "))
uint = input("(L)bs or (K)gs: ")
if uint.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")
