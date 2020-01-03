import random
def GenerateRandomNumber():
    random.seed()
    x = random.randint(1,10)
    return x

def UserEntry():
    valid = False
    while valid == False:
        try:
            userInput = input("Guess a number between 1 and 10 inclusive:")
            val = int(userInput)
            valid = True
        except ValueError:
            print("That's not an int!")
            valid = False
    return val

ranNum = GenerateRandomNumber()
print("Please guess a number between 1 and 10 (Inclusive)")
guessCorrect = False
while guessCorrect == False:
    guess = UserEntry()
    if guess == ranNum:
        guessCorrect = True
    elif guess > ranNum:
        print("Lower")
    elif guess < ranNum:
        print("Higher")
print("Correct! The random number was: " + str(ranNum))





