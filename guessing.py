import random 

print "This is the Guessing Game!!"

name = raw_input("Hi!  What's your name? ") 

print "Hi, %s!" % name
print "%s, I'm thinking of a random number between 1 and 100. Try to guess my number." % name

answer =  random.randint(1,100)

print "The answer is %d." % answer 

guess = int(raw_input("Your guess? ")) 

while guess != answer:
    
    if guess > answer:
    
        print "Your guess is too high.  Try again."
          
        guess = int(raw_input("Your next guess?"))  

    elif guess < answer:
        
        print "Your guess is too low.  Try again."

        guess = int(raw_input("Your next guess?"))  
   
    elif guess == answer:
        
        print "That's the correct guess!  Yay, you win everything!"
        
        break

