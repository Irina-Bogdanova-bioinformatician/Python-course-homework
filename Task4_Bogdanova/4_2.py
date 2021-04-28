my_list = input("Введите числа через запятую ").split(",")
new_list = [int(a) for a in my_list]
final_list = [i for i in new_list if new_list.count(i) == 1]
print(final_list)
input('\nPress ENTER to exit')
