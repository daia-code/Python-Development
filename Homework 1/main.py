# create a list
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# copy first list in another list
my_listOrd = my_list.copy()

# # list sort ascendent
my_listOrd.sort()
print(my_listOrd[:])

# list sort descendent
my_listOrd.sort(reverse=True)
print(my_listOrd)

# print even numbers of list
my_sliced_list_Even = my_listOrd[::2]
print(my_sliced_list_Even)

# print odd numbers of list
my_slice_list_Odd = my_listOrd[1::2]
print(my_slice_list_Odd)

# print multiples of the number  3
my_slice_list_3 = my_listOrd[1::3]
print(my_slice_list_3)
