SERVICE_CHARGE = 2
TICKET_PRICE = 10

tickets_remaining = 100

# Create the calculate_price function. It takes number of tickets and returns
# num_ticktes * TICKET_PRICE
def calculate_price(num):
    # Create a constant for the service charge
    # Add the service charge to our result
    return (num * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining:

    print("There are {} tickets remaing".format(tickets_remaining))
    name = input("What is your name? ")
    num_ticktes = input("How many tickets would you like, {}? ".format(name))
    # Expect a ValueError to happen and handle it appropriately...remember to
    # test it out
    try:
        num_ticktes = int(num_ticktes)
        # Raise a ValueError if the request is for more tickets than are avilable
        if num_ticktes > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        print("Oh no, we ran into an issue. Please try again".format(err))
    else:
        total_price = calculate_price(num_ticktes )
        print("The total price is ${}".format(total_price))
        should_proceed = input("Do you want to proceed? : Y/N  ")
        # Gather credit card information and process it
        if should_proceed.lower() == "y":
            print("SOLD!")
            tickets_remaining -= num_ticktes
        else:
            print("Thank you anyways {}!".format(name))

# Notify the user that the tickets are sold out
print("Sorry, tickets are sold out")










