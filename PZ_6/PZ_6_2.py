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
    print(spisok)
number = - 1
for i in range(1,N -1):
    if spisok[i] > spisok[i - 1] and spisok[i] > spisok[i+1]:
        number = i + 1
if number != -1:
    print("Номер локал максимума:",number)
else:
    print("Локального максимума нету в списке.")


