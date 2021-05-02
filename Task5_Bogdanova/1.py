data = "Hello!"
data_list = []
while data != "":
    data = input("Введите данные ")
    data_list.append(data)
with open("text_1.txt", "w") as customer_text:
    for line in data_list:
        customer_text.writelines(line+"\n")
print("Файл записан")
