import re

salary = open("text_3.txt", "r", encoding="utf8")
salary.seek(0)
lines_list = salary.readlines()
total_salary = 0
number = 0
lowest_salary = []
for i in lines_list:
    number += 1
    worker_salary = int(re.sub(r"\D", "", i))
    total_salary += worker_salary
    if worker_salary < 20000:
        worker_surname = re.sub(r"[^A-zА-я]", "", i)
        lowest_salary.append(worker_surname)
print("Средняя величина доходов сотрудников: ", total_salary / number)
print("Фамилии работников, имеющих оклад менее 20000: ", lowest_salary)
salary.close()
