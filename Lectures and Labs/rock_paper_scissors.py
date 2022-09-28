import random

rock = "rock"
paper = "paper"
scissors = "scissors"

user = input("Please enter [rock, paper, scissors]: ")
cpu = random.randint(1, 3)

# change cpu value from number into rock paper or scissors
if cpu == 1:
    cpu = rock
elif cpu == 2:
    cpu = paper
else:
    cpu = scissors

# Print Result

# if user chooses rock
if user == rock and cpu == rock:
    print(f"CPU chooses {cpu}")
    print("Tie")
elif user == rock and cpu == paper:
    print(f"CPU chooses {cpu}")
    print("CPU Win")
elif user == rock and cpu == scissors:
    print(f"CPU chooses {cpu}")
    print("You Win")

# if user chooses paper
elif user == paper and cpu == rock:
    print(f"CPU chooses {cpu}")
    print("You Win")
elif user == paper and cpu == paper:
    print(f"CPU chooses {cpu}")
    print("Tie")
elif user == paper and cpu == scissors:
    print(f"CPU chooses {cpu}")
    print("CPU Win")

# if user chooses scissors
elif user == scissors and cpu == rock:
    print(f"CPU chooses {cpu}")
    print("CPU Win")
elif user == scissors and cpu == paper:
    print(f"CPU chooses {cpu}")
    print("You Win")
elif user == scissors and cpu == scissors:
    print(f"CPU chooses {cpu}")
    print("Tie")
else:
    print("Invalid Input")

