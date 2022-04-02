def read():
    try:
        n = int(input("Enter something:"))
    except ValueError:
        print("Is not a integer")
        return 0
    else:
        return n


def main():
    n = read()
    print(n)


main()
