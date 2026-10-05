import random
while True:
    player_choice = input("Choose rock,paper,scissor:")
    choices=["rock","paper","scissor"]
    computer_choice=random.choice(choices)
    print(computer_choice)
    if computer_choice== player_choice:
        print("Its a tie")
    elif computer_choice=="rock":
        if player_choice=="paper":
            print("You Won")
            break
        else:
            print("You Lose")
    elif computer_choice=="paper":
        if player_choice=="scissor":
            print("You Won")
            break
        else:
            print("You Lose")
    else:
        if player_choice=="rock":
            print("You Won")
            break
        else:
            print("You Lose")