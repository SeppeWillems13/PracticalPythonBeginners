import random

roll = random.randint(1, 6)
guess = int(input("Guess the dice roll: "))

if guess == roll:
    print("You won! they rolled a " + str(roll))
else:
    print("You lost! they rolled a " + str(roll))
