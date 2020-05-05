# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]

try:
    number = int(input("Введите число (пустое значение прерывает цикл): "))
except ValueError:
    number = False

while number:
    try:
        position = my_list.index(number)
        count = my_list.count(number)
        my_list.insert(position + count, number)
    except ValueError:
        for i in my_list:
            if number > i:
                my_list.insert(my_list.index(i), number)
                break
        else:
            my_list.append(number)
    print(my_list)
    try:
        number = int(input("Введите число (пустое значение прерывает цикл): "))
    except ValueError:
        number = False