def string_check (choice, options):

    is_valid = ""
    chosen = ""

    for var_list in options:

        # if the snaclk is in one of the lists, return the full statement
        if choice in var_list:

            # get full name of snack and put it
            #in title case so it looks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break
        
        # if the chosen option is not valid, set is_valid to no
        else:
            is_valid = "no"

    # if the snack is not OK - ask question again
    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"

def instructions (options):
    show_help = "invalid choice"
    while show_help == "invalid choice":
        show_help = input ("Would you like to read the instructions?: ").lower()
        show_help = string_check (show_help, options)

    if show_help == "Yes":
        print ()
        print ("*** Fund Raising Calculator Instructions ***")
        print ()
        print ("This program will ask you for...")
        print ("- The name of the product you are selling")
        print ("- The number of items you are planning to sell")
        print ("- The costs for each component of the product")
        print ("- Your profit goal")
        print ()
        print ("It will then display a list of the other costs \n"
               "with subtotals for the variable and fixed costs. \n"
               "The program will tell you how much you should sell \n"
               "each item for to reach your profit goal")
        print ()
        print ("The data will also be written to a text file which \n"
               "has the same name as your product")

    return ""

# main routine goes here
# list for valid yes / no responses
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]


# aks if instructions are needed
instructions (yes_no)
print ()
print ("*** Program launched ***")