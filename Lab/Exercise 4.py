time = int(input("Enter the number of seconds: "))

hour = time // 3600
minute = time % 3600 // 60
sec = time % 60

print (f"Result: {hour}:{minute}:{sec}")
