from itertools import cycle

first_list = input("Введите числа через запятую ").split(",")
a = 0
for i in cycle(first_list):
    if a < 20:
        print(i)
        a += 1
    else:
        break
input('\nPress ENTER to exit')
