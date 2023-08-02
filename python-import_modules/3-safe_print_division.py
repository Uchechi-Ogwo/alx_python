# A function that divides 2 integers and print the result

def safe_print_division(a, b):
  try:
    result = a / b
  except ZeroDivisionError:
    print("Error: Cannot be divide by zero!")
    return None
  except Exception as e:
    print("Error:", e)
  finally:
    try:
      print("Inside result: {}".format(result))
    except NameError:
      print("Inside result: Division resulted in an error.")
    return result