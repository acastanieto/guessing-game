import random 

print "This is the Guessing Game!!"

name = raw_input("Hi!  What's your name? ") 

print "Hi, %s!" % name
print "%s, I'm thinking of a random number between 1 and 100. Try to guess my number." % name

answer =  random.randint(1,100)

print "The answer is %d." % answer 

#guess = int(raw_input("Your guess? ")) 

while True:
    try:
        guess = int(raw_input("Your guess?" ))
        break
    except ValueError:
        print "Oops! That was no valid number! Try again."

while guess != answer:
    
    if guess < 0 or guess > 100:

        print "Your guess is out of bounds, please try again." 
   
        guess = int(raw_input("Your next guess?"))


    elif guess > answer:
    
        print "Your guess is too high.  Try again."
          
        guess = int(raw_input("Your next guess?"))  

    elif guess < answer:
        
        print "Your guess is too low.  Try again."

        guess = int(raw_input("Your next guess?"))

else:
        
    print "That's the correct guess!  Yay, you win everything!"
        


