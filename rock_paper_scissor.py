import random

computer_choice = random.choice(["rock", "paper", "scissors"])

user_choice = input("Enter your choice: ")

if user_choice == computer_choice:
    print("Tie!")
elif user_choice == "rock":
    if computer_choice == "paper":
        print("You lose!")
    else:
        print("You win!")
elif user_choice == "paper":
    if computer_choice == "scissor":
        print("You lose!")
    else:
        print("You win!")
elif user_choice == "scissor":
    if computer_choice == "rock":
        print("You lose!")
    else:
        print("You win!")

print("Computer chose " + computer_choice)