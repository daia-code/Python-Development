cnp = []
ok = False

def dict_get_value(s, cnp_0):
    for keys, value in s.items():
        if cnp_0 in keys:
            return value
    return None

def birth_year(cnp):
    saa = {('1', '2', '7', '8', '9'): 1900, ('3', '4'): 1800, ('5', '6'): 2000}
    days_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    year = dict_get_value(saa, cnp[0]) + int(cnp[1:3])
    month = int(cnp[3:5])
    day = int(cnp[5:7])

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days_month[2] = 29
    return 1 <= month <= 12 and 1 <= day <= days_month[month]

def control(cnp):
    num = '279146358279'
    sum = 0

    ### SUM & MODULO ###
    for i in range(0, 12):
        sum = sum + int(cnp[i]) * int(num[i])
    c = sum % 11
    if c == 10:
        c = 1
    ### OUTPUT ###

    if c == int(cnp[12]):
        return True
    else:
        return False

while not ok:
    ok = True
    cnp = input("Te rugam sa introduci condul numeric personal:")
    if cnp[0] == 0 or len(cnp) != 13 or not cnp.isdigit():
        print("Cod numeric personal invalid.")
        ok = False


    elif not birth_year(cnp):
        ok = False
    elif int(cnp[7:9]) not in range(1, 53):
        ok = False
    elif cnp[9:12] == '000':
        ok = False
    elif not control(cnp):
        ok = False
    elif not ok:
        print("CNP gresit")

print("Ai introdus un CNP Valid.")