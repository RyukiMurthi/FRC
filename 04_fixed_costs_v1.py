import pandas

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
                            "The price must be a wgole number more than 0",
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


# *** main routine starts here ***

# get product name
product_name = not_blank ("Product name: ", "The product name can't be blank")

fixed_expenses = get_expenses ("fixed")
fixed_frame = fixed_expenses [0]
fixed_sub = fixed_expenses [1]

# *** printing area ***

print ()
print (fixed_frame [['Cost']])
print ()

print ("Fixed costs: ${: .2f}".format (fixed_sub))