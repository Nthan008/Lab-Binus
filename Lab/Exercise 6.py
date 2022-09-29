burger = int(input("Enter burger selling price: "))
soda = int(input("Enter soda selling price: "))
combo = int(input("Enter combo meal selling price: "))

price = (burger + soda) - combo
print(f"The fixed price is ${price}.00")