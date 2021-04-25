def int_func(the_word):
    """ Принимает слово из маленьких латинских букв и возвращающает его же, но с прописной первой буквой.

    Именованный параметр:
    the_word -- слово, введенное пользователем (str)
    Программа возвращает слово в виде строки (str).

    """
    return the_word.capitalize()


word_list = input('Введите слова, состоящие из маленьких латинских букв, через пробел ').split(" ")
final_string = str()
for new_word in word_list:
    if new_word.isdigit():
        final_string += new_word
        final_string += " "
    else:
        a = int_func(new_word)
        final_string += a
        final_string += " "
if len(final_string) > 0:
    print(final_string[:-1])
else:
    print("Вы не ввели слова")
input('\nPress ENTER to exit')
