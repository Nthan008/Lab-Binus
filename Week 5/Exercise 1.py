
def convert_to_days():
    hour= int(input("Enter number of hours: "))
    minute= int(input("Enter number of minutes: "))
    second= int(input("Enter number of seconds: "))
    days = get_days(hour, minute, second)
    print (round(days, 4))

def get_days(hour, minute, second):
    return(hour/24 + minute / 1440 + second / 86400)

convert_to_days()