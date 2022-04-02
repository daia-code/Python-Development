def your_function():
    return 0


def your_function2(p1, p2, p3, *args):
    s = p1 + p2 + p3
    return s


def your_function3(p1, p2, *args, **kargs):
    s = p1 + p2
    return s


def main():
    nr1 = your_function2(1, 5, -3, 'abc', [12, 56, 'cad'])
    print(nr1)
    nr2 = your_function()
    print(nr2)
    nr3 = your_function3(2, 4, 'abc', param_1=2)
    print(nr3)


main()
