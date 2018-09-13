first_name = input("What is your first name?  ")
print("Hello,", first_name)
if first_name == "Shaun":
    print(first_name, "is learning Python")
elif first_name == "Barbara":
    print(first_name, "is not learning Python")
else:
    scale = int(input("On a scale of 1 to 10, how busy are you?  "))
    if scale <= 10:
        print("Wow you're at a {}! If you're bored, you should learn Python".format(scale))
    print("Or do some work, {}!".format(first_name))
print("Have a good day {}!".format(first_name))