# Дан список размера n. Найти номер его последнего локального максимума.
from random import*
n = int(input("Введите размер списка:"))
A = []
x = 0
for i in range(n):
    A.append(randint(1,10))
print(A)
for i in range(1,n):
    if A[i] > A[i-1] and A[i] > A[i+1]:
        x = i
if x != 0:
    print(f"Номер последнего локального максимума:{x}")
else:
    print("Локальных максимумов нету.")