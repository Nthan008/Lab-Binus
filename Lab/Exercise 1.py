bill = int(input("Enter amount of bill: "))
people = int(input("Enter number of people: "))
tips = int(input("Enter amount of tips(%): "))

total_bill = bill / people
total_tips = tips/100 * bill / people

print(f"Bill and tips per person are ${total_bill} and ${total_tips} USD")