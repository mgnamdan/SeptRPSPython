import random

#   1. Get a choice from the computer -> save it somewhere (x)
#   2. Get a choice from the player -> save it somewhere (x)
#   3. Compare the two choices
#   4. Determine and announce a winner

#   1 --> Rock
#   2 --> Paper
#   3 --> Scissors

compChoice = random.randint(1, 3)

playerChoice = input("Make a choice (rock/paper/scissors): ")

if playerChoice == "rock":
    if compChoice == 1:
        # P: rock, C: rock; Tie
        print("You and the computer both chose rock! You tie!")
    elif compChoice == 2:
        # P: rock, C: paper; Lose
        print("You chose rock and the computer chose paper! You lose!")
    else:
        # P: rock, C: scissors; Win
        print("You chose rock and the computer chose scissors! You win!")


elif playerChoice == "paper":
    if compChoice == 1:
        # P: paper, C: rock; Win
        print("You chose paper and the computer chose rock! You win!")
    elif compChoice == 2:
        # P: paper, C: paper; Tie
        print("You and the computer both chose paper! You tie!")
    else:
        # P: paper, C: scissors; Lose
        print("You chose paper and the computer chose scissors! You lose!")


elif playerChoice == "scissors":
    if compChoice == 1:
        # P: scissors, C: rock; Lose
        print("You chose scissors and the computer chose rock! You lose!")
    elif compChoice == 2:
        # P: scissors, C: paper; Win
        print("You chose scissors and the computer chose paper! You win!")
    else:
        # P: scissors, C: scissors; Tie
        print("You and the computer both chose scissors! You tie!")


else:
    print("Invalid choice!")