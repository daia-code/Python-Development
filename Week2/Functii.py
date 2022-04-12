# print("Message on console")
# variabila = 1
# print("Message no {}".format(variabila))
# raspuns_utilizator = input("Enter your name:")
# print(raspuns_utilizator)

# def my_function(param_1):
#     pass

# def suma(a: int, b: int = 6)->(int,int):
#     """
#
#     :param a:
#     :param b:
#     :return:
#     """
#     if type(a) == str:
#         return a
#     return a + b
#
#
# my_sum = suma('1', 4)
# print(my_sum)

# def my_function(*param_1):
#     print(type(param_1))
#     return param_1
#
# print(my_function("string","string1","string2"))

# def suma_nr_infinite(param1, param2=1, *var):
#     suma = 0
#     for item in var:
#         suma += item
#     return suma
#
#
# print(suma_nr_infinite(1, 2, 3, 4, 5, 6, 7,))
#
# def catalog(*args, **kwargs):
#     print(type(kwargs))
#     return args, kwargs
#
#
# print(catalog(1,'a',nume="Ion", prenume="Vasile", varsta="12"))

# def suma(a,b):
#     a=diferenta(a,b)
#     return a + b
#
#
# def diferenta(a,b):
#     return a - b
#
#
# print(suma(diferenta(10, 2),2)) # ctrl+d


# print(suma(1, 2))

# a, b = 10, 20
# min = None
# # if a < b:
# #     min = a
# # else:
# #     min = b
# min = a if a < b else b
# print(min)

lista_produse = ["ciocolata", "suc", "paine", "mere", "apa"]
# lista_noua=[]
# for x in lista_produse:
#     if "a" in x:
#         lista_noua.append(x)
# lista_noua = [x for x in lista_produse if "a" in x]
# print(lista_noua)
# a = 10
# b = 1
# min = None
# if min := a < b: print(min)
# else:
#     min = b

import datetime

data = '05/07/05'
print(datetime.datetime.strptime(data, "%d/%m/%y"))
