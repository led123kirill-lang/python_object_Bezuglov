#Дан список размера N. Переставить в обратном порядке элементы список,
#расположенный между его максимальным и минимальным элементами
#включая минимальныйи максимальный элементы.
from random import*
n = int(input("Введите размер списка:"))
A =[]
for i in range(n):
    A.append(randint(1,10))
print(A)
min_i = A.index(min(A))
max_i = A.index(max(A))

d = min(min_i,max_i)
b = max(min_i,max_i)

A[d:b + 1] = A[d:b + 1][::-1]
print(A)