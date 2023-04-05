"""
Topics Covered:
- Lists (append, pop)
- For and while loops
- Getting user inputs
- Validating user inputs
- Functions and helper functions
- Formatted Strings
"""

# import random to generate a random number
# import math to round number
import random
import math

def print_welcome_and_menu(list_of_toppings, list_of_sizes, list_of_prices):
    # print welcome message
    print("Welcome to Meow Meow Pizza Stand!")
    print()
    print("Our toppings are: ")
    # go through the topping list, print one by one topping
    for flavor in list_of_toopings:
        print(topping, end="\n")
    print()
    # go through the length of the pizza size list
    # use the same index from the size list to access the price list
    # print messages including sizes equivalent to prices
    for i in range(len(list_of_sizes)):
        print("Our {} pizza is ${}".format(list_of_sizes[i], list_of_prices[i]))
    print()


def get_order_qty(customer_name):
    """
    Ask the customer how many orders of pizza they want.
    Valid order quantity should be an integer 1-5 inclusive. If outside the range or non-int, re-prompt.
    If the input is a float, Example: 2.54 will return 2 and follow the rules of string to integer casting.
    Returns: How many orders of pizza the customer wants.
    """
    # using While loop, allow users to reenter unlimited times until it met criteria
    while True:
        qty_input = input("Hi " + customer_name + " how many pizza will you be ordering (1 to 5)? ")
        # using try except to catch inputs are not int
        # round down to the closet int
        # condition to break the while loop is when int(input) in between 1 and 5
        try:
            order_qty = int(math.floor(float(qty_input)))
            if order_qty in range(1, 6):
                return order_qty
                break
            else:
                continue
        except ValueError:
            print('Sorry, the input is not an int.  Please try again.')


def get_pizza_topping(pizza_toppings):
    """
    Ask the customer 'Which topping would you like (v/c/s)? '
    Then, processes and cleans the input and returns the equivalent topping from pizza_topping list.
    Returns: String of pizza topping picked (e.g "ham")
    """
    # create a variable for question, use this variable as an argument, pass it into get_first_letter_of_user_input parameter
    # check get_first_letter_of_user_input output value, using index to access into pizza_toppings list to get associated flavor
    # loop back the question if users enter invalid input
    while True:
        topping_picked = ""
        topping_question = "Which flavor would you like (v/c/s)? "
        first_letter_topping = get_first_letter_of_user_input(topping_question)
        try:
            if first_letter_topping == "v":
                topping_picked = pizza_toppings[0]
                return topping_picked
                break
            elif first_letter_topping == "c":
                topping_picked = pizza_toppings[1]
                return topping_picked
                break
            elif first_letter_topping == "s":
                topping_picked = pizza_toppings[2]
                return topping_picked
                break
            else:
                continue
        except ValueError:
            print("Error")


def get_pizza_size(pizza_sizes):
    """
    Ask the customer 'Which size would you like (s/m/l)? '
    Then, processes and cleans the input and returns the equivalent size from pizza_sizes list.
    Returns: String of Size picked (e.g "Small")
    """
    # create a variable for question, use this variable as an argument, pass it into get_first_letter_of_user_input parameter
    # check get_first_letter_of_user_input output value, using index to access into pizza_sizes list to get associated sizes
    # loop back the question if users enter invalid input
    while True:
        size_picked = ""
        size_question = "Which size would you like (s/m/l)? "
        first_letter_size = get_first_letter_of_user_input(size_question)
        try:
            if first_letter_size == "s":
                size_picked = pizza_sizes[0]
                return size_picked
                break
            elif first_letter_size == "m":
                size_picked = pizza_sizes[1]
                return size_picked
                break
            elif first_letter_size == "l":
                size_picked = pizza_sizes[2]
                return size_picked
                break
            else:
                continue
        except ValueError:
            print("Error")


def get_pizza_order_price(pizza_size, pizza_prices, pizza_sizes):
    """
    Returns: The equivalent price of an pizza size. Example: Returns 4.99 if pizza_size is 'Small'
    """
    # get picked_size pizza index
    # use that index to get price associated with it
    # return picked pizza price
    index = pizza_sizes.index(pizza_size)
    pizza_price = pizza_prices[index]
    return pizza_price


def take_customer_order(customer_name, pizza_toppings, pizza_sizes, pizza_prices):
    """
    This function runs when a customer reaches the front of the queue. It should print
    the current customer's name being served, and take their order(s).
    If the customer can pay for their order, returns the amount of revenue from the sale.
    If the customer cancels their order, returns 0.
    Returns: Amount of Revenue from the sale with customer
    """

    total_bill = 0

    print("Now serving customer: ", customer_name)
    order_qty = get_order_qty(customer_name)

    for order in range(order_qty):
        print("Order No.:", order + 1)
        picked_topping = get_pizza_topping(pizza_toppings)
        picked_size = get_pizza_size(pizza_sizes)
        picked_topping_size_price = get_pizza_order_price(picked_size, pizza_prices, pizza_sizes)
        total_bill = total_bill + picked_flavor_size_price
        print("You ordered a {} {} for ${}".format(picked_size, picked_topping, picked_topping_size_price))

    print("Your total bill is: $", total_bill)
    while True:
        pay_or_cancel_question = "Would you like to pay or cancel the order (p/c)? "
        first_letter_size = get_first_letter_of_user_input(pay_or_cancel_question)
        try:
            if first_letter_size == "p":
                return total_bill
                break
            elif first_letter_size == "c":
                total_bill = 0
                return total_bill
                break
            else:
                continue
        except ValueError:
            ValueError


def get_first_letter_of_user_input(question):
    """
    Takes in a string as its argument, to be used as the question you want the user to be asked.
    Gets input from the user, removes whitespace and makes all letters lowercase
    Returns: The first letter of the input the user provides. Ask again if the input is empty.
    """
    # create a func with a parameter, pass an argument into the func
    # cast the input to str, remove spaces head and tail by using strip()
    # if the valid is Not an empty str, get only the first index and convert to lower case
    # else, continue the loop
    while True:
        user_input = input(question)
        try:
            user_input = str(user_input).strip()
            if user_input != "":
                first_letter = user_input[0].lower()
                return first_letter
                break
            else:
                continue
        except ValueError:
            print("Error")


def are_all_customers_served(customer_queue_length):
    """
    If there are no customers in the queue, returns True, and all customers have been served.
    Otherwise, returns False.
    Returns: True or False
    """
    # if the queu is equal to 0, return True, else False
    if customer_queue_length == 0:
        return True
    else:
        return False


def print_current_status(customers_served, tracking_revenue):
    """
    Prints a message of how many customers have been served and the total sales of the pizza stand.
    """
    print("We have now served {} customer(s), and received ${} in revenue".format(customers_served, tracking_revenue))


def print_sales_summary(customers_served, tracking_revenue):
    """
    Takes in the arguments customers_served and tracking_revenue. Prints both
    arguments as strings to let the user know what those values are.
    Output should look something like:
        Total customers served: 3
        Total sales           : $xx.xx
    """
    print("Total customers served:\t", customers_served,
          "\nTotal sales:\t\t", tracking_revenue)


def random_queue_length():
    """
    Takes no arguments.
    Uses the imported randint function to generate a random integer between 2 and 5 inclusive.
    Returns: The resulting random integer.
    """
    # generate a random number for the queue
    random_queue = random.randint(2, 5)
    return random_queue


def main():
    """
    Lists of available toppings, sizes and prices.
    For sizes and prices, we will use the following convention:
    Index 0 for Small
    Index 1 for Medium
    Index 2 for Large
    """
    pizza_toppings = ['Chesse', 'Mushroom', 'Onion']
    ice_cream_sizes = ['Small', 'Medium', 'Large']
    ice_cream_prices = [4.99, 7.49, 8.49]

    # List of names of possible customers
    customer_names = ["Wongwong", "Kiki", "Pigie", "TN", "MeowMeow"]

    program_running = True
    while program_running:
        # set shop to open
        input('Press any key to open the shop! ')
        queue_is_open = True

        #  pizza_flavors, pizza_sizes, pizza_prices
        print_welcome_and_menu(pizza_toppings, pizza__sizes, pizza__prices)
        # set initial values
        tracking_revenue = 0

        # will hold the list of names of the customers in the queue
        customers_in_queue = []
        customers_served = 0

        num_of_customers_in_queue = random_queue_length()

        print("Num of customers in queue: ", num_of_customers_in_queue)
        #   Then, append each name to the end of the customers_in_queue list.
        #   The total number of customer names added should be equal to num_of_customers_in_queue
        #   Note: It is OK to have duplicate names in the queue.
        for i in range(num_of_customers_in_queue):
            customers_in_queue.append(random.choice(customer_names))
        while queue_is_open:
            #  the current_customer_name variable.
            #  After extraction, the customer should now be removed from the customers_in_queue list.
            current_customer_name = customers_in_queue[0]
            customers_in_queue.pop(0)
            tracking_revenue += take_customer_order(current_customer_name, pizza__toppings, pizza__sizes, pizza__prices)
            customers_served += 1
            print_current_status(customers_served, tracking_revenue)
            #  customers in the queue.
            #  If False, continue the loop.
            #  If True, call the print_sales_summary(customers_served, tracking_revenue) and close the queue
            if are_all_customers_served(len(customers_in_queue)) == True:
                print_sales_summary(customers_served, tracking_revenue)
                break
            else:
                continue
        #  Update the program_running variable if you get a valid answer either 'y' or 'n'
        #  Otherwise, re-prompt until a valid answer is given
        while queue_is_open:
            open_queue_again = "Do you want to open again (y/n)? "
            first_letter_size = get_first_letter_of_user_input(open_queue_again)
            try:
                if first_letter_size == "y":
                    program_running = True
                    break
                elif first_letter_size == "n":
                    program_running = False
                    break
                else:
                    continue
            except ValueError:
                ValueError
if __name__ == '__main__':
    main()
