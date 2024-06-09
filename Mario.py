#shows the use of nested for loops

#we COULD print just 3 "#" as bricks
print("#")
print("#")
print("#")

#this loop does the same as above
for _ in range(3):
    print("#")

#using functions and loops, we can do the same that can be expanded by height of any n # of bricks
def main():
    print_column(3) #prints 3 "#" as bricks using the function loop below


def print_column(height):
    for _ in range(height):
        print("#")

def main(): 
    print_row(4) #prints "?" as bricks 4 x


def print_row(width): #takes width instead of height
    print("?" * width)
main()


##for a 3x3 grid of bricks
def main():
    print_square(3)


def print_square(size):

    # For each row in square
    for i in range(size):

        # For each brick in row, or prints columns
        for j in range(size): #nested for loop

            #  Print brick
            print("#", end="")

        # Print blank line, moves cursor to new line, acts as \n when print is blank
        print()


main()

#more compact way of writing the above
def main():
    print_square(3) #prints 3 x


def print_square(size):
    for i in range(size):
        print_row(size)


def print_row(width):
    print("#" * width)


main()

