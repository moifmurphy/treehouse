import math

def split_check(total, number_of_people):
    if number_of_people <= 1:
        raise ValueError("More than 1 person is required to split the bill")
    return math.ceil(total / number_of_people)

try:
    total_due = float(input("What is the total?  "))
    number_of_people = int(input("How many people stuffed their faces?  "))
    amount_due = split_check(total_due, number_of_people)
except ValueError:
    print("Computer says No, try again")
    print("{}").format(err)
else:    
    print("Each person owes £{}, pay up bitches".format(amount_due))
