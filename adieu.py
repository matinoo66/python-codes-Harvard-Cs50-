import inflect
p = inflect.engine()

#create a list to keep track of names
names = []
#loop forever
while True:
    try:
        #get user input
        name = input("Name: ")
        names.append(name)
    except EOFError:
        #create a new line and stop The Loop
        print()
        break
        #printing using inflect module
output = p.join(names)
print("Adieu, adieu, to " + output)
