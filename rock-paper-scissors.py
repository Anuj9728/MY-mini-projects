import random

user_wins=0
computer_wins=0
options=["rock","paper","scissor"]
while True:
    user_input=input("write Rock / Paper / scissor or Q to quite the program : ").lower()
    if user_input == "q":
        print("you won",user_wins,".")
        print("computer won" ,computer_wins,".")
        quit()
    elif user_input not in options:
        print("enter a valid option")
        continue

    random_int=random.randint(0,2)
    computer_input=options[random_int]
    print("computer picked",computer_input+".")

    if user_input==computer_input:
        continue

    if user_input == "rock" and computer_input == "scissor":
        print("you won!")
        user_wins += 1
    elif user_input =="paper" and computer_input =="rock":
        print("you won!")
        user_wins += 1
    elif user_input =="scissor" and computer_input =="paper":
        print("you won!")
        user_wins += 1
    else:
        print("you lost!")
        computer_wins += 1


