import random 

print "This is the Guessing Game!!"

name = raw_input("Hi!  What's your name? ") 

print "Hi, %s!" % name
print "%s, I'm thinking of a random number between 1 and 100. Try to guess my number." % name

answer =  random.randint(1,100)

print "The answer is %d." % answer 

#guess = int(raw_input("Your guess? ")) 

play = True

while True:
    try:
        guess = int(raw_input("Your guess?" ))
        break
    except ValueError:
        print "Oops! That was no valid number! Try again."


while play == True:
    
    if guess < 0 or guess > 100:

        print "Your guess is out of bounds, please try again." 
   
        while True:
            try:
                guess = int(raw_input("Your guess?" ))
                break
            except ValueError:
                print "Oops! That was no valid number! Try again."


    elif guess > answer:
    
        print "Your guess is too high.  Try again."
          
        while True:
            try:
                guess = int(raw_input("Your guess?" ))
                break
            except ValueError:
                print "Oops! That was no valid number! Try again."  

    elif guess < answer:
        
        print "Your guess is too low.  Try again."

        while True:
            try:
                guess = int(raw_input("Your guess?" ))
                break
            except ValueError:
                print "Oops! That was no valid number! Try again."

    elif guess == answer:
                
        print "That's the correct guess!  Yay, you win everything!"
        playAgain = raw_input("Do you want to play again?  Type yes or no.")
        if playAgain != "yes" and playAgain != "no":
            playAgain = raw_input("Please type yes or no.")
        elif playAgain == "yes":

            answer =  random.randint(1,100)

            print "The answer is %d." % answer 

            while True:
                try:
                    guess = int(raw_input("Ok, let's play again. Your guess?" ))
                    break
                except ValueError:
                    print "Oops! That was no valid number! Try again."
        else:
            play = False
            print "Ok, thanks for playing!"

        


