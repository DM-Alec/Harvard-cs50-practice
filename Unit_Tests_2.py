#from hello.py
#hello world code from first lecture
def main():
    name = input("What's your name? ")
    hello(name)


def hello(to="world"):
    print("hello,", to)


if __name__ == "__main__":
    main()

#how do we test this

#from test_hello.py
from hello import hello


def test_hello():
    assert hello("David") == "hello, David"#*
    assert hello() == "hello, world"

#*this will not work as the function will not return a value    


#we can fix this by changing 
#hello.py
def main():
    name = input("What's your name? ")
    print(hello(name))

def hello(to="world"):
    return f"hello, {to}"

if __name__ == "__main__":
    main()


#test_hello.py
from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("David") == "hello, David"

   