# from <filename> import <class>
from Author import Author
from Book import Book
def main():
    a1 = Author("RR", "rr@rr.com", 'M')
    a2 = Author("RJ", "rj@rj.com", 'F')
    
    myBuku = Book("Abdul's Adventures",[a1,a2],100)
    
    print(myBuku.toString())
       
if __name__ == "__main__":
    main()
    
    

