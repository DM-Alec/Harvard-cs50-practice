#We can use a folder full of tests 
#from terminal
#mkdir test
#code test/test_hello.py

from hello import hello
  
  
def test_default():
    assert hello() == "hello, world"
  
  
def test_argument():
    assert hello("David") == "hello, David"

