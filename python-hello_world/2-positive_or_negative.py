import random

# Generate a random signed number between -100 and 100 (inclusive)
number = random.randint(-100, 100)

# Check if the number is positive, negative, or zero, and print the result
if number > 0:
    print("{}: is positive".format(number))
elif number == 0:
    print("{}: is zero".format(number))
else:
    print("{}: is negative".format(number))