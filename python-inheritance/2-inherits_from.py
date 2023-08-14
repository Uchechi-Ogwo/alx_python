""" 
This Module is issubclass method takes the obj type variable,
and a_class method
"""


def is_kind_class(obj, a_class):
    """ 
    Function to check if a data is a subclass of the other
    This function takes two numbers, 'obj' and 'a_class',
    and returns a bool if it was inherited from it class.

       Parameters:
           obj (field): The first number.
           a_class ( object): The second number.

       Return:
           bool (True and False): from the comparison of obj and a_class

    """
    # if isinstance(type(obj), a_class)
    if isinstance(type(obj), a_class) or issubclass(type(obj), a_class):
        return True
    else:
        return False