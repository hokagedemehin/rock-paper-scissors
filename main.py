# from random import choices
import random


def rock_paper_scissors():
    """
    Rock Paper Scissors
    """
    print(
        """
    Welcome to Rock Paper Scissors
    Please enter your choice:
    - R for Rock
    - P for Paper
    - S for Scissors
    """
    )
    user_choice = input("Enter your choice: ")
    if user_choice == "r" or user_choice == "R":
        user_choice = "Rock"
    elif user_choice == "p" or user_choice == "P":
        user_choice = "Paper"
    elif user_choice == "s" or user_choice == "S":
        user_choice = "Scissors"
    else:
        print("Invalid Choice")
        rock_paper_scissors()

    computer_choice = random.choice(["Rock", "Paper", "Scissors"])

    # print(f"You chose {user_choice} and the computer chose {computer_choice}")

    if user_choice == computer_choice:
        print(f"Player ({user_choice}) : CPU ({computer_choice})")
        print("It's a tie")
        rock_paper_scissors()
    elif user_choice == "Rock":
        if computer_choice == "Paper":
            print(f"Player ({user_choice}) : CPU ({computer_choice})")
            print("You lose")
        else:
            print(f"Player ({user_choice}) : CPU ({computer_choice})")
            print("You win")
    elif user_choice == "Paper":

        if computer_choice == "Scissors":
            print(f"Player ({user_choice}) : CPU ({computer_choice})")
            print("You lose")
        else:
            print(f"Player ({user_choice}) : CPU ({computer_choice})")
            print("You win")
    elif user_choice == "Scissors":
        if computer_choice == "Rock":
            print(f"Player ({user_choice}) : CPU ({computer_choice})")
            print("You lose")
        else:
            print(f"Player ({user_choice}) : CPU ({computer_choice})")
            print("You win")
    # else:
    #     print("Invalid Choice again")
    # rock_paper_scissors()


if __name__ == "__main__":
    rock_paper_scissors()
