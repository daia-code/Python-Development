# print("Message on console")
# variabila = 1
# print("Message no {}".format(variabila))
# raspuns_utilizator = input("Enter your name:")
# print(raspuns_utilizator)

# def my_function(param_1):
#     pass

def suma(a: int, b: int = 6)->(int,int):
    """

    :param a:
    :param b:
    :return:
    """
    if type(a) == str:
        return a
    return a + b


my_sum = suma('1', 4)
print(my_sum)
