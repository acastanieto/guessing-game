print "This is the Guessing Game!!"

name = raw_input("Hi!  What's your name? ") 

print "Hi, %s!" % name
print "%s, I'm thinking of a random number between 1 and 100. Try to guess my number." % name
print "Try to guess my number."

guess = raw_input("Your guess? ") 

import random 

answer =  random.randint(1,100)

print answer 
