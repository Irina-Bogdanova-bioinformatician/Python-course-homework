import re

with open("text_2.txt", "r") as new_text:
    new_text.seek(0)
    lines_list = new_text.readlines()
    a = 1
    word_amount = []
    for i in lines_list:
        b = re.sub(r"[^A-zА-я ]", "", i)
        c = b.split(" ")
        d = [x for x in c if x != '']
        word_amount.append(f"{a}: {len(d)}")
        a += 1
    print("Число строк в файле:", len(lines_list))
    print("Количество слов в каждой строке (строка: количество слов):", word_amount)
