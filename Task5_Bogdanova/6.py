import re

academic_disc = open("text_6.txt", "r", encoding="utf8")
academic_disc.seek(0)
lines_list = academic_disc.readlines()
final_dict = {}
for i in lines_list:
    subject = re.sub(r"[^A-zА-я ]", "", i)
    a = subject.split(" ")
    f = [x for x in a if x != '' and x != "л" and x != "пр" and x != "лаб"]
    b = ""
    for el in f:
        b += el
        b += " "
    b = b[:-1]
    amount = re.sub(r"\D", " ", i)
    c = amount.split(" ")
    d = [x for x in c if x != '']
    g = 0
    for e in d:
        e = int(e)
        g += e
    final_dict[b] = g
print(final_dict)
academic_disc.close()
