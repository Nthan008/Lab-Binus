amt = int(input("Enter an amount: "))
inter = float(input("Enter the rate of interest: "))
year = int(input("Enter the number of years: "))
i = 0
while i != year:
    amt = amt + inter/100*amt
    i += 1
amt = "{:.2f}".format(amt)
print (amt)