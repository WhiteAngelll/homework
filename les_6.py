# Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

goods = []

counter = 1
question = input("Добавить элемент? (y/n): ")

if question == "y":
    question = True
else:
    question = False

while question:
    name = input("Введите имя товара: ")
    price = input("Введите цену товара: ")
    count = input("Введите количество товара: ")
    unit = input("Введите единицу измерения товара: ")
    element = (counter, {"Название": name, "Цена": price, "Количество": count, "Единицы": unit})
    goods.append(element)
    counter += 1

    question = input("Добавить элемент? (y/n): ")
    if question == "y":
        question = True
    else:
        question = False

names = []
prices = []
counts = []
units = []

for good in goods:
    good_tuple = good[1]
    names.append(good_tuple["Название"])
    prices.append(good_tuple["Цена"])
    counts.append(good_tuple["Количество"])
    units.append(good_tuple["Единицы"])

result = {"Название": names, "Цена": prices, "Количество": counts, "Единицы": units}
print(result)