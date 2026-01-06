from cgi import print_arguments
import random
#0=rock
#1=paper
#2=scissers
#user_input = int(input("choose Rock,Paper and Scissors :"))
user_choice = int(input("Enter your choose type 0 for Rock,1 for Paper and 2 for Scissors :"))
if user_choice  >= 3 or user_choice <0 :
    print("invalid number you lose")
else:
    computer_choice = random.randint(0,2)
    print(computer_choice)
    if user_choice == 0 and computer_choice == 2:
        print("you win")
    elif user_choice == 2 and computer_choice == 0:
        print("you lose")
    elif computer_choice > user_choice:
        print("you lose")
    elif user_choice > computer_choice:
        print("you win")
    elif user_choice == computer_choice:
         print("its a draw")
