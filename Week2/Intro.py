message = "Ana\'s have  oranges"
print(message)
no_orange = 2
message = f'Ana\'s have {no_orange} oranges'  # the most usable
print(message)
no_cherr = 5
message = "Ana have {0} oranges and {1} cherries".format(no_orange, no_cherr)
print(message)

list = [4, 2, 3, 'Ana', 5]
print(list[0:2:1])
list[0] = 10
print(list[:])

# tuple1 = (1)  # immutable
# print(type(tuple1))  # one element is like int
tuple = (1, -3, 'a')  # selectors django are tuple

dictionary = {"key1": 1, "key2": 2}
print(dictionary.get("key3", 3))
print(dictionary)
dictionary["key3"] = 3
print(dictionary)
dictionary.update({"key4": 4})
print(dictionary.values())
print(dictionary.keys())
print(dictionary.items())

set1 = {"item", 1, 2, 3}  # immutable
set2 = {"item", 2, -1}
print(set1.intersection(set2))
print(set1.union(set2))
print(set2.difference(set1))

my_var = 3
m = "conditii false"
if my_var < 5:
    m = "mai mic"
elif my_var > 4:
    m = "mai mare"

print(m)

variabila_1 = 1
while variabila_1 < 3:
    print("Instruction")
    variabila_1 = variabila_1 + 1

cuvant = "Ana are mere"
for x, value in enumerate(cuvant):
    print(x, value)

for i in range(0, 10, 2):
    print(i)
