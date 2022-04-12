# def my_function():
#     global msg
#     msg = "Hello"
#     print(msg)
#     return None
#
#
# print(msg)
# print(my_function())
# print(dir(my_function()))
# print(msg)

def my_function():
    def my_second_function():
        global msg
        msg = "Hello"
        print(print(locals()), "my second function")
        return None

    my_second_function()
    # print(msg)
    msg = "Hello World!"
    print(f"principal function {msg}")
    return None


my_function()
# print(msg)
print(globals())
