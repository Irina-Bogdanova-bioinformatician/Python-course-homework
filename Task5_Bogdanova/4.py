with open("text_4.txt", "r") as new_text:
    new_text.seek(0)
    lines_list = new_text.readlines()
    changed_list = []
    final_list = []
    for i in lines_list:
        new_list = i.split(" ")
        for element in new_list:
            if element == "One":
                element = "Один"
            elif element == "Two":
                element = "Два"
            elif element == "Three":
                element = "Три"
            elif element == "Four":
                element = "Четыре"
            changed_list.append(element)
        final_string = " ".join(changed_list)
        final_list.append(final_string)
        changed_list.clear()
with open("text_4_2.txt", "w") as result_text:
    for line in final_list:
        result_text.writelines(line)
