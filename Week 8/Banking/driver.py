from Bank import Bank
from Account import Account
from Customer import Customer
def main():
    b1 = Bank("BCA")
    
    b1.addcustomer("Switch", "Era")
    
    print (b1.getnumOfCust())
    print(b1.getcustomers(0).getlastName())

if __name__ == "__main__":
    main()