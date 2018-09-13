import math

def split_check(total, number_of_people):
    return math.ceil(total / number_of_people)


total_due = float(input("What is the total?  "))
number_of_people = int(input("How many people stuffed their faces?  "))
amount_due = split_check(total_due, number_of_people)

print("Each person owes £{}, pay up bitches".format(amount_due))