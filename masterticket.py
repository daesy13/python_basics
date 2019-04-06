TICKET_PRICE = 10

tickets_remaining = 100

# Output how many tickets remaing using the tickets_remaining variable
print("There are {} tickets remaing".format(tickets_remaining))

# Gather the user's name and assign it to a new variable
name = input("What is your name? ")

# Prompt the user by their name and ask how many tkts they would like
num_ticktes = input("How many tickets would you like, {}? ".format(name))
num_ticktes = int(num_ticktes)

# Calculate the price(#tkts * price) and assign it to a variable
total_price = num_ticktes * TICKET_PRICE

# Output the price to the screen
print("The total price is ${}".format(total_price))

# Prompt user if they want to proceed Y/N
should_proceed = input("Do you want to proceed? : Y/N  ")

# if they want to proceed
if should_proceed.lower() == "y":
    # print out SOLD! to confirm purchase
    # and decrement tkts remaining
    print("SOLD!")
    tickets_remaining -= num_ticktes

# Otherwise...
else:
    # thank them by name
    print("Thank you anyways {}!".format(name))
