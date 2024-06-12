
#exception to get rid of answers like "cat" that are not integers
try:
    x = int(input("What is x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")


#Name Error 
#a problem with your code syntax
try:
    x = int(input("What is x? "))# int func error
    
except ValueError:
    print("x is not an integer")   


print(f"x is {x}")# x is not not copied to x here


#using "else" with try/except
try:
    x = int(input("What is x? "))# int func error
    
except ValueError:
    print("x is not an integer")   
else:
    print(f"x is {x}")# x is not not copied to x here
    

#improving using loops
while True:    
    try:
        x = int(input("What is x? "))
    
    except ValueError:
        print("x is not an integer")   
    else: #associated w "try" NOT the loop
        break
    
print(f"x is {x}")
    

#get int method
def main():
    x = get_int()
    print (f"x is {x}")
    
def get_int():
    while True:    
        try:
            x = int(input("What is x? "))
            
        except ValueError:
            print("x is not an integer")   
            
        else: #associated w "try" NOT the loop
            return x #will break out of loops AND return val

main ()
    

 #dont technically need the else
def main():
    x = get_int()
    print (f"x is {x}")
    
def get_int():
    while True:    
        try:
            x = int(input("What is x? "))
        except ValueError:
            print("x is not an integer")   #less obvious of whats going on

main ()  


#pass function to not have it print out "x is not an int" constantly
def main():
    x = get_int()
    print (f"x is {x}")
    
def get_int():
    while True:    
        try:
            x = int(input("What is x? "))
        except ValueError:
            pass #though doesn't give reason why it keeps prompting now

main () 


#final refinements
#not hard code x, parameter for main to use the get x function
def main():
    x = get_int("What's x? ")# doesnt have to know whats being asked just asks the prompt
    print (f"x is {x}")
    
def get_int(prompt):#
    while True:    
        try:
            x = int(input(prompt)) # uses prompt
        except ValueError:
            pass 

main () 


#can also raise codes, talked about in lecture 4