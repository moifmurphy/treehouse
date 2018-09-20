SERVICE_CHARGE = 2
TICKET_PRICE = 10

tickets_remaining = 100

# Create a function to calculate the ticket price and add a service charge
def calculate_price(number_of_tickets):
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

# Loop this code until the tickets sell out
while tickets_remaining >= 1:

    # Ouput how many tickets are remaining using the tickets_remaining variable
    print("There are {} tickets remaining.".format(tickets_remaining))

    # Gather the user's name and assign it to a new variable
    name = input("What is your name?  ")

    # Prompt the user by name and ask how many tickets they would like
    num_tickets = input("How many tickets would you like, {}?  ".format(name))

    try:
        # Expect a ValueError here
        num_tickets = int(num_tickets)
        # Expect a ValueError if the request is for more tickets than are available
        if num_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets left".format(tickets_remaining))
    except ValueError as err:
        # Error text included in the output
        print("Are you sure? {}. Please try again".format(err))
    else:    

        # Calculate the price (number of tickets they want multiplied by the price) and assign that to a variable
        amount_due = calculate_price(num_tickets)

        # Output the price to the screen
        print("The total due is £{}".format(amount_due))

        # Prompt user and ask if they want to proceed: Y/N
        should_proceed = input("Do you want to proceed?  Y/N  ")


        # If they do want to proceed
        if should_proceed.lower() == "y":

            # Gather credit card information


            # Confirm purchase
            print("Confirmed")

            #Reduce the number of tickets remaining (decrement)
            tickets_remaining -= num_tickets

        # If they do not want to proceed, say thanks
        else:
            print("Thank you anyway, {}".format(name))

# Notify users that the tickets have all sold out
print("Sorry, we've sold out for this event :(")