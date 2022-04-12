variable = input("Enter a number:")

try:
    is_integer = int(variable)
except ValueError as e:
    print("Error at value ", e)
except Exception as e:
    #print(e.__doc__)
    print("You have a error at  ", e)
