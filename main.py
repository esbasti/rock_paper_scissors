
#Variables Definition
import random

userValue = 0
userItem = ""

computerValue = 0
computerItem = ""

#Introduction to the game
print("Welcome to the game Rock Paper Scissors")

# Picking the item based on integers 1,2 or 3
# If invalid value return error message
def definePick(input):
    if input == "1":
        return 1, "Scissors"
    elif input == "2":
        return 2, "Rock"
    elif input == "3":
        return 3, "Paper"
    else:
        return 0, ""

#User selection
while userValue == 0:
    print("Choose one of the following options:")
    print("Type 1 for scissors")
    print("Type 2 for rock")
    print("Type 3 for paper")
    userInput = input("")
    (userValue, userItem) = definePick(userInput)
    if userValue == 0:
        print("Wrong input, please try again")

# Selecting computer choice
(computerValue, computerItem) = definePick(str(random.randint(1,3)))

#Present choices to the user
print("You picked: " + userItem)
print("The computer picked: " + computerItem)

#Logic to decise the winner
if computerItem == "Paper" and userItem == "Scissors":
    print("Congratulations, you win!!!")
elif computerItem == "Rock" and userItem == "Paper":
    print("Congratulations, you win!!!")
elif computerItem == "Scissors" and userItem == "Rock":
    print("Congratulations, you win!!!")
elif computerItem == "Paper" and userItem == "Rock":
    print("Sorry, you loose. :(")
elif computerItem == "Rock" and userItem == "Scissors":
    print("Sorry, you loose. :(")
elif computerItem == "Scissors" and userItem == "Paper":
    print("Sorry, you loose. :(")
else:
    print("It is a tie")
