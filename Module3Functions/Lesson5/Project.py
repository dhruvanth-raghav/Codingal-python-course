import random
player=0
comp = 0

while True:
    choice = input("Rock, paper or scissors: ")
    computer = random.choice(["rock", "paper", "scissors"])
    print("Computer chose:", computer)

    if choice == computer:
        print("Tie!")
        #"or/"-chooses any one in the following
    elif(choice == "rock" and computer == "scissors") or \
        (choice == "paper" and computer == "rock") or \
        (choice == "scissors" and computer == "paper"):
        print("You win!")
        player+=1
    else:
        print("Computer wins!")
        comp = comp + 1

    print("Score:-You:",player,"Computer:",comp)
    again = input("Wanna play again? (yes/no)")
    if again == "no":
        break
       



