import random

comp_value = random.randrange(1000, 9999)                                                                        
user_value = int(input("Guess the four numbers computer will print: "))

if user_value == comp_value:
    print("Wow! You are genius")
elif user_value < comp_value:                             print("You are below the Computer prediction value of {}".format(comp_value))
else:                                                     print("You are above the Computer prediction value of {}".format(comp_value))
