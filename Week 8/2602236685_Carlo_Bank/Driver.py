from Account import Account
from Customer import Customer
from Bank import Bank
def main():
    role = input("For admin enter 0, for customer enter 1: ")
    if (role=='0'):
        print("Welcome admin")

    elif (role=='1'):
        print("Welcome dear customer")
        act = input("Press 0 to login, press 1 to register: ")
        if (act == '0'):
            user = input("Enter your username: ")   
            if (user in Customer):
                pin = input("Enter your pass: ")
        elif (act == '1')  :
            user = input("Enter your username: ")   
            if (user in Customer):
                setPin(input("Enter your pin: "))   
                  
            
        
        
    else:
        print("incorrect input")
        
        b1 = Bank("BCA")
        
        #adding a customer to the bank
        b1.addCustomer("Laplace", "AnyLastName")
        b1.addCustomer("Andrew", "Tanenbaum")
        b1.addCustomer("Vania", "Vanilla")
        
        #getting the total number of customers
        print(b1.getNumOfCust())
        
        #accessing info of a customer
        print(b1.getCustomer(2).getFirstName())
        print(b1.getCustomer(2).getLastName())
        
        #create an account for a customer
        b1.getCustomer(2).setAccount(Account(500000))
        
        print(b1.getCustomer(2).getAccount().getBalance())
        
        if b1.getCustomer(2).getAccount().deposit(1000000):
            print(b1.getCustomer(2).getAccount().getBalance())
        else:
            print("Invalid")
        
    
    
    
    
if __name__ == "__main__":
    main()
    
    

