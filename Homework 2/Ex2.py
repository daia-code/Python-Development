def sum_of_nr(nr):
    s = 0
    s_Even = 0
    s_Odd = 0
    for i in range(0, nr + 1):
        s = s + i
        if i % 2 == 0:
            s_Even = s_Even + i
        else:
            s_Odd = s_Odd + i

    print("The sum is ", s)
    print("The sum of even numbers is ", s_Even)
    print("The sum of odd numbers is ", s_Odd)


def main():
    try:
        nr = int(input("Enter a integer:"))
        sum_of_nr(nr)
    except ValueError:
        print("The number must be a integer")
    else:
        print("The code work!")


main()
