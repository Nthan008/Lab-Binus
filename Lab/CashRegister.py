bills = [100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]

def cash_register(price, cash):
    change = cash - price
    num = 0
    count = 0
    change_bills = []
    while True:
        for i in bills:
            if i > change:
                num = bills[count-1]
                change -= bills[count-1]
                count = 0
                change_bills.append(num)
                break
            count += 1
        if change <= 0:
            break 
    return (change_bills)

print(cash_register(10990, 11000))



