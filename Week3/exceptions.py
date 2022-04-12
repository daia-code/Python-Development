variable = input("Enter a number:")
my_int = None
try:
    is_integer = int(variable)
    print("no exceptions at meeting")
    if my_int is None:
        raise ValueError
except ValueError as e:
    print("Error at value ", e)
except Exception as e:
    # print(e.__doc__)

    print("You have a error at  ", e)
else:
    print("no exceptions at meeting")
finally:
    print("Compile...")
