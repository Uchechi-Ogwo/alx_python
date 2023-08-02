def divide_and_print_result(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot be divided by zero!")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    else:
        print("Result: {}".format(result))
        return result

# Test cases
result1 = divide_and_print_result(10, 2)  # Result: 5.0
result2 = divide_and_print_result(10, 0)  # Error: Cannot be divided by zero!
result3 = divide_and_print_result(0, 5)   # Result: 0.0
