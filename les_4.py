# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

string = input("Введите строку из нескольких слов, разделённых пробелами: ")

for word in enumerate(string.split(), 1):
    if len(word[1]) < 11:
        print(f"{word[0]}) {word[1]}")
    else:
        print(f"{word[0]}) {word[1][:10]}")