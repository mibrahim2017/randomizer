import random
print("choose rock, paper, or scissors")
rps=["rock", "paper", "scissors"]

while True:
    computer=random.choice(rps)
    player=str(input("enter rock, paper, or scissors: ")).lower()
    print(f"you chose {player} and computer chose {computer}")
    if computer==player:
        print("it's a tie!")
    elif player=="rock" and computer=="scissors":
        print("you win! rock crushes the scissors")
    elif player=="paper" and computer=="rock":
        print("you win! paper captures the rock")
    elif player=="scissors" and computer=="paper":
        print("you win! scissors cuts the paper")
    elif computer=="rock" and player=="scissors":
        print("you lose. rock crushes the scissors")
    elif computer=="paper" and player=="rock":
        print("you lose. paper captures the rock")
    elif computer=="scissors" and player=="paper":
        print("you lose. scissors cuts the paper")    
    else:
        print("invalid choice")
    choice=str(input("do you want to continue?(y or n)")).lower()
    if choice=="n":
        print("goodbye, thank you for playing rock paper and scissors")
        break
