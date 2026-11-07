#Дан список размера N. Переставить в обратном порядке элементы список,
#расположенные между его минимальным и максимальным элементами, включая
#минимальный и максимальный элементы.

import random
try:
    N = int(input("Введите размер списка:"))
except ValueError:
    print("Вводите целые числа!")
spisok = []
i = 0
while i < N:
    spisok.append(random.randrange(1,9))
    i += 1
print("Исходный список:",spisok)
min_index = spisok.index(min(spisok))
max_index = spisok.index(max(spisok))
if min_index > max_index:
    min_index,max_index = max_index,min_index
spisok[min_index:max_index + 1] = spisok[min_index:max_index + 1][::-1]
print("Изменненый список:",spisok)
