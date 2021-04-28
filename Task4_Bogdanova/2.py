my_list = input("Ведите числа через запятую ").split(",")
new_list = [float(i) for i in my_list]
comparison_list = new_list.copy()
comparison_list.pop(0)
final_list = [b for a, b in zip(new_list, comparison_list) if a < b]
print(final_list)
