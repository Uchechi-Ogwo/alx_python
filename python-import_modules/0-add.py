# Import the add function from add_0.py
from add_0 import add

# Assign values to variables a and b
a = 1
b = 2

# Call the add function with a and b as arguments and store the result in a variable called result
result = add(a, b)

# Print the result using string formatting
print("{} + {} = {}".format(a, b, result))

if __name__ == "__main__":
  main()