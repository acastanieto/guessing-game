import random

def guessprompt():
    while True:
        try:
            guess = int(raw_input("Your guess? " ))
            return guess
        except ValueError:
            print "Oops! That was no valid number! Try again."

def generateRandomNumber(testing):
    answer =  random.randint(1,100)
    if testing == True:
        print "(The answer is %d.)" % answer
    return answer


print "This is the Guessing Game!!"


test_mode = raw_input("Are you playing in test mode, yes or no? ")
test_mode = test_mode.lower()

testing = False
if test_mode == "yes":
    testing = True
elif test_mode == "no":
    testing = False

name = raw_input("Hi!  What's your name? ")
print "Hi, %s!" % name

print "%s, I'm thinking of a random number between 1 and 100. Try to guess my number." % name

play = True

answer = generateRandomNumber(testing)

guess = guessprompt()

guesscount = 0

while play == True:

    guesscount += 1

    if guess < 0 or guess > 100:
        print "Your guess is out of bounds, please try again."
        guess = guessprompt()

    elif guess > answer:
        print "Your guess is too high.  Try again."
        guess = guessprompt()


    elif guess < answer:
        print "Your guess is too low.  Try again."
        guess = guessprompt()

    elif guess == answer:
        print "That's the correct guess!  Yay, you win everything!"
        print "You took %d guesses to win." % guesscount

        playAgain = raw_input("Do you want to play again?  Type yes or no. ")
        playAgain = playAgain.lower()

        if playAgain != "yes" and playAgain != "no":
            playAgain = raw_input("Please type yes or no. ")

        elif playAgain == "yes":
            print "Ok, let's play again!"

            guesscount = 0

            answer = generateRandomNumber(testing)

            guess = guessprompt()

        else:
            play = False
            print "Ok, thanks for playing!"
