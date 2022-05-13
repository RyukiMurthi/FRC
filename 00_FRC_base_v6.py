# import libraries
import pandas
import math


# *** Functions go here ***

# checks that input is either a float or an
# integer that is more than zero. Takes in custom error message
def num_check (question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print (error)
            else:
                return response

        except ValueError:
            print (error)


#function to check name is not blank
def not_blank (question, error):
   
    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print ("{}.     \nPlease try again.\n".format(error))
            continue
            
        return response

# currency formatting function
def currency (x):
    return "${: .2f}".format (x)

# gets expenses, returns list which has
# the data frame and subtotal
def get_expenses (var_fixed):
    # set up dictionaries and lists

    item_list = []
    quantity_list = []
    price_list = []

    variable_dict = {
        "Item": item_list,
        "Quantity": quantity_list,
        "Price": price_list
    }

    # loop to get component, quantity and price
    item_name = ""
    while item_name.lower () != "xxx":

        print ()
        #get name, quantity and item
        item_name = not_blank ("Item name: ",
                            "The component name can't be blank")
        if item_name.lower () == "xxx":
            break

        if var_fixed == "variable":
            quantity = num_check ("Quantity: ",
                            "The amount must be a whole number more than 0",
                            int)

        else:
            quantity = 1

        price = num_check ("How much?: $",
                            "The price must be a whole number more than 0",
                             float)

        # add item, quantity and price to lists
        item_list.append (item_name)
        quantity_list.append (quantity)
        price_list.append (price)

    expense_frame = pandas.DataFrame (variable_dict)
    expense_frame = expense_frame.set_index ('Item')

    # calculate cost of each component
    expense_frame ['Cost'] = expense_frame ['Quantity']\
                            * expense_frame ['Price']

    # find subtotal
    sub_total = expense_frame ['Cost'].sum ()

    # currency formatting (uses currency function)
    add_dollars = ['Price', 'Cost']
    for item in add_dollars:
        expense_frame [item] = expense_frame [item].apply (currency)

    return [expense_frame, sub_total]

def expense_print (heading, frame, subtotal):
    print ()
    print ("*** {} Costs ***".format(heading))
    print (frame)
    print ()
    print ("{} Costs: ${: .2f}".format(heading, subtotal))
    return ""

def profit_goal (total_costs):

    # intialise variabkes and error message
    error = "Please enter a valid profit goal\n"

    valid = False
    while not valid:

        # ask user for profit goal...
        response = input ("What is your profit goal (eg $500 or 50%): ")

        # check if first character is $...
        if response [0] == "$":
            profit_type = "$"
            # get amount (everything after $)
            amount = response [1:]

        # check if last character is %
        elif response [-1] == "%":
            profit_type = "%"
            # get amount (Eeverything before %)
            amount = response [:-1]

        else:
            # set response to amount for now
            profit_type = "unknown"
            amount = response

        try:
            # check amount is a number more than zero...
            amount = float (amount)
            if amount <= 0:
                print (error)
                continue

        except ValueError:
            print (error)
            continue
        
        if profit_type == "unknown" and amount >= 100:
            dollar_type = yes_no ("Do you mean ${: .2f}.   "
                                  "ie {: .2f} dollars?, "
                                  "yes / no: ".format (amount, amount))

            # set profit type based on user answer above
            if dollar_type == "yes":
                profit_type = "$"
            else:
                profit_type = "%"

        elif profit_type == "unknown" and amount < 100:
            percent_type = yes_no ("Do you mean {}%?, "
                                   "yes / no: ".format (amount))
            if percent_type == "yes":
                profit_type = "%"
            else:
                profit_type = "$"

        # return profit goal to main routine
        if profit_type == "$":
            return amount
        else:
            goal = (amount / 100) * total_costs
            return goal

def round_up (amount, round_to):
    return int (math.ceil (amount / round_to)) * round_to

def string_check (choice, options, error):

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
        print(error)

def instructions (options):
    show_help = string_check ("Do you want to see the instructions", options, "please enter yes / no")

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
instructions(yes_no)
print ()
print ("*** Program launched ***")
print ()

# *** main routine goes here ***

# get product name
product_name = not_blank ("Product name: ", "The product name can't be blank")

how_many = num_check ("How many items will you be producing?: ", 
                      "The number of items must be a whole" 
                      "number more than 0", int)

print ()
print ("Please enter your variable costs below...")
# get variable costs
variable_expenses = get_expenses ("variable")
variable_frame = variable_expenses [0]
variable_sub = variable_expenses [1]

print()
have_fixed = string_check("Do you have fixed costs (y/n)?: ", yes_no, "Please enter yes / no")

if have_fixed == "yes":
    # get fixed costs
    fixed_expenses = get_expenses ("fixed")
    fixed_frame = fixed_expenses [0]
    fixed_sub = fixed_expenses [1]
else:
    fixed_sub = 0

# work out total costs and profit target
all_costs = variable_sub + fixed_sub
profit_target = profit_goal (all_costs)

# calculate total sales needed to reach goal
sales_needed = all_costs + profit_target

# ask user for rounding
round_to = num_check ("Round to the nearest...?: ", "Can't be 0", int)

# calculate recommended price
selling_price = sales_needed / how_many
print ("Selling Price (unrounded): "
       "${: .2f}".format (selling_price))

recommended_price = round_up (selling_price, round_to)

# write data to file

# *** Printing area ***

print ()
print ("*** Fund Raising - {} ***".format (product_name))
print ()
expense_print ("Variable", variable_frame, variable_sub)

if have_fixed == "yes":
    expense_print ("Fixed", fixed_frame [['Cost']], fixed_sub)

print ()
print ("*** Total Costs: ${: .2f} ***".format (all_costs))
print ()

print ()
print ("*** Profit and Sales Targets ***")
print ("Profit Target: ${: .2f}".format (profit_target))
print ("Total Sales: ${: .2f}".format (all_costs + profit_target))

print ()
print ("*** Pricing ***")
print ("*** Minimum Price: ${: .2f}".format (selling_price))
print ("Recommended Price: ${: .2f}".format (recommended_price))