def yes_no (question):
    
    valid = False
    while not valid:

        # ask question and put response in lowercase
        response = input (question).lower()

        if response == "y" or response == "yes":
            return "yes"
        elif response == "n" or response == "no":
            return "no"
        
        else:
            print ("Please enter either yes / no...\n")

# loops to make testing faster...
for item in range (0,6):
    want_help = yes_no ("Do you want to read the instructions?: ")
    print ("You said '{}\n".format (want_help))