from collections import Counter

my_list = input("Введите числа через запятую ").split(",")
new_list = [int(a) for a in my_list]
final_list = [x for x, i in Counter(new_list).items() if i == 1]
print(final_list)
input('\nPress ENTER to exit')
