x = int(input("What's x? "))

#used for remainders, if remainder is 0, or not divided evenly by 2, then odd
#if x % 2 == 0:
 #   print("Even")
#else:
 #   print("Odd")

 #boolean method, returns true or false
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    if n % 2 == 0:
        return True #bool, must be capitalized T and F
    else:
        return False


main()


#pythonic method, can only be seen in python code
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    return n % 2 == 0 #you can collapse if else into just return


main()


