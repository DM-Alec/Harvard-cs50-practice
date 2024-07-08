
#Unit tests

#this program is called calculator
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n # n + n BUG INPUT FROM BELOW

#this convention to only conditionally calling main
if __name__ == "__main__":
    main()



#we import the above to use as a test in the code below
from calculator import square


def main():
    test_square()


def test_square():
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squared was not 9")


if __name__ == "__main__":
    main()

#if we test this, nothing outputs
#we purposely add a bug in calculator of changing n * n to n + n   
#but now we only see 1 error of 2* 2 since it is still technically true 2*2 == 2 + 2 
   
#this test is longer to write than the actual code were testing so we use
#ASSERT

from calculator import square


def main():
    test_square()


def test_square():
    assert square(2) == 4 # assert func allows to tell compiler that some assertion is true
    assert square(3) == 9


if __name__ == "__main__":
    main()

#however there is an error on asser square3 == 9 now due to specificities
# unfortuantely the fix is burdensome

from calculator import square


def main():
    test_square()


def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared is not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared is not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squared is not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squared is not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared is not 0")


if __name__ == "__main__":
    main()

#this amount of coding is not ideal for a test
#to test code easier we use
#
#PYTEST

from calculator import square


def test_assert():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0

#pytest is 3rd party library that we install with pip install pytest
#from terminal:
#pytest test_calculator.py
#
#this will show Fail "F" or Pass "." and will show you the lines it failed at    

#calculator.py file
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n #change this to show fail "+" or not


if __name__ == "__main__":
    main()

#same setup buyt separated out, making it easier to see what is failing
from calculator import square


def test_positive():
    assert square(2) == 4
    assert square(3) == 9 #will show fail here


def test_negative():
    assert square(-2) == 4 #will show fail here
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError): #tests string inputs and raises typeError
        square("cat")