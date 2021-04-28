from itertools import count

first_number = int(input("Введите целое число "))
a = 0
for i in count(first_number):
    if a < 20:
        print(i)
        a += 1
    else:
        break
input('\nPress ENTER to exit')
