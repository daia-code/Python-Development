cuvant = "alfabet"
# cuvant = 'a__a__t'
cuvant_ascuns = []
for i in cuvant:
    # print(cuvant[0],cuvant[-1])
    if cuvant[0] != i and cuvant[-1] != i:
        cuvant_ascuns.append('_')
    else:
        cuvant_ascuns.append(i)
print("".join(cuvant_ascuns))
count_nr = 1
set_litere_deja_incercate = set()
while count_nr <= len(cuvant):

    user_letter = input("Alege o litera: ")
    # print(user_letter)
    if user_letter in set_litere_deja_incercate:
        print("Litera deja incercata")
        continue
    if user_letter in cuvant:
        for iterator, value in enumerate(cuvant):
            # print(iterator,value)
            if cuvant[iterator] == user_letter:
                cuvant_ascuns[iterator] = user_letter
        print(" ".join(cuvant_ascuns))
    else:
        count_nr = count_nr + 1

    if '_' not in cuvant_ascuns:
        print("Ai castigat!")
        break

    elif count_nr == len(cuvant):
        print(f'Ai pierdut! Cuvantul era {cuvant}')
    set_litere_deja_incercate.add(user_letter)

