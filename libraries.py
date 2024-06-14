#Random
import random
import stat #import the random library
	
coin = random.choice(["heads", "tails"]) #random.choice(sequence or list used here)
print(coin)

#downside is typing random.choice all the time

from random import choice # this changes the scope to choice and will load it into the functions

coin = choice(["heads", "tails"])
print(coin)


#random.randint(a,b) 
# list of integers from a to b
import random
num = random.randint(1,10)
print(num)

#random.shuffle(x) 
#shuffles the integers or list
import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards: #for ea card on that list, print one card
    print(card)
    

#statistics library (mean, medians, modes)
#calc avg
import statistics

print(statistics.mean([100,90])) #list of two vals will, print mean


#system function
#sys.argv argument vector, describes list that user typed in before they hit enter
import sys

try:
    print("hello, my name is", sys.argv[1]) # takes element in list

except IndexError:
    print("Too few arguments")
    

#we can use conditionals to make it more defensive
import sys

if len(sys.argv) < 2:
    print("Too few arguments") # lower bound lim
elif len(sys.argv) > 2:
    print("Too many arguments") # upper bound lim
else:
    print("hello, my name is", sys.argv[1])

   #keeping the error check by itself away from the code can simplify it further
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments") #we can intro sys.exit to exit the code prematurely
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1]) # this will give NameError if sys.exit isnt used
#blindly calls list as it does not exit the code and never execute the print func


#Slice
#for a list greater than a single name
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv:
    print("hello, my name is", arg) #this will print all the names however
    
#to get a single part of a list we use Slice
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]: #brackets for Slice [start at element 1: (blank)] slices off first part of list
    print("hello, my name is", arg)

#we can add -1 to lsice off the end of the list within the brackets for the Slice command
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:-1]: # slices off the first and last object of the list
    print("hello, my name is", arg)



