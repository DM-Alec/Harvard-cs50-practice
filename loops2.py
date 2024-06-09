#improving user input for loops
while True:
    n = int(input("What's n? ")) #inducing infinite loop until what we want is given
    if n < 0:
        continue
    else:
        break #stops the loop that its in


#continue is redundant so we can improve
while True:
    n = int(input("What's n? "))
    if n > 0: #need + value to continue to for loop below
        break

for _ in range(n): #prints n range until break in loop
    print("meow")


#loops using functions
def main():
    meow(get_number()) #runs getnumber function below for user input


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 1: # only runs loop function below if greater than 1
            return n # can use break, but we need return to have input value for loop func below


def meow(n):
    for _ in range(n):#uses user input range and prints meow said n times
        print("meow")


main()


