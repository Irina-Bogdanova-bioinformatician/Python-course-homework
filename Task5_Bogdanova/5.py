new_numbers = input("Введите числа через пробел ")
total = 0
n = 0
with open("text_5.txt", "w+") as numbers:
    print(new_numbers, file=numbers)
    numbers.seek(0)
    string_numbers = numbers.read()
    list_numbers = string_numbers.split(" ")
    for i in list_numbers:
        if i == "\n" or i == "":
            print("Вы ввели лишний пробел")
            break
        else:
            a = float(i)
            total += a
            n += 1
    if n == len(list_numbers):
        print("Сумма чисел: ", total)
