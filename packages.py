#we can donwload more packages from pypi.org
#pip is a package manager program that comes w python itself that manages the packages you download
#from terminal: pip install cowsay
#this will download the cowsay package
import cowsay #package is on lypi.org/project/cowsay
import sys

if len(sys.argv) == 2: # wont print anything if nothing is typed
    cowsay.cow("hello, " + sys.argv[1]) #concatinate w + in order to pass string
#this prints out an ASCII pic of a cow saying the name

#APIs
#App program interface, refer to 3rd party services that you can write code to talk to


#api of a Weezer song
#can do this manually by entering a url, which leads to a JSON  
#JSON
#javacript object notation, used as language agnostics format (can be read by any program lang) 
import requests
import sys

if len(sys.argv) != 2: #error check, if no band is entered, the code exits
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(response.json()) #makes sure data we retrieve is formatted from JSON and converts to python


#python has built in json library that can interpret JSON
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(json.dumps(response.json(), indent=2)) #dumps = dump string: indent by at least 2 spaces

#We can isolate to just list the track name that we picked from the JSON file
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
#changed number of songs to list to 50 within the url search term----------^
o = response.json()
for result in o["results"]: #iterates in order to find what we want
    print(result["trackName"])#lists the track name from JSON


#we can make our own libraries
#good practice is to make a library of code you often use and calling said library to avoid rewriting
#sayings.py file code:    
def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")

#once this is created, we can make a new file and type
import sys

from sayings import goodbye #this will import sayings.py file made above, no retyping code

if len(sys.argv) == 2:
    goodbye(sys.argv[1])

# cannot blindly call main from saying.py file so we use this to correct sayings.py
#sayings.py file code:    
def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")
    
if __name__ == "__main__": #__name__ var used when running file from command line
    main() # name is auto set to name of module saying.py when imported
