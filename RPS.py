import random
computer_score = 0 
player_score = 0
while computer_score < 3 and player_score < 3:
    print(f"Player Score : {player_score} Computer Score : {computer_score}")
    print("Player 1's turn")
    a = input("Rock\nPaper\nScissors\nyour choice : ").lower()
    print("NOTE : if you wanna quit press q or exit")
    if a == 'q' or a == 'exit':
        break
    mylist = ["rock", "paper", "scissors"]
    computer = random.choice(mylist)
    print(f"The computer plays: {computer}")
    if a == computer:
        print("It's a tie!")
    elif a == "rock":
        if computer == "paper":
            print("Computer wins :( ")
            computer_score += 1
        else:
            print("Player wins!")
            player_score += 1
    elif a == "paper":
        if computer == "rock":
            print("Player win!")
            player_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
    elif (a == "scissors"):
        if (computer == "rock"):
            print("Computer wins!")
            computer_score += 1
        else:
            print("You win!")
            player_score += 1
    else:
        print("Please enter a valid move!")   
if player_score > computer_score:
    print("Congrats You've Won!")
elif player_score == computer_score:
    print("It's a TIE!")
else:
    print("Computer Won!")