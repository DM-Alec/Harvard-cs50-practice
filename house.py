name = input("What's your name? ")

#given a name, will print what house said person is in
if name == "Harry":
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == "Ron": 
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?") # if other names are entered
    

#another way to do this that is more compact
name = input("What's your name? ")

if name == "Harry" or name == "Hermione" or name == "Ron": 
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")
    
    
    #match statements method of this code
name = input("What's your name? ")

match name: 
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron": 
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
        
    #more compact match state ver
name = input("What's your name? ")
match name: 
    case "Harry" | "Hermione" | "Ron": #can use | to say "or"
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")