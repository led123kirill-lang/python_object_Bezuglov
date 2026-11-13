A = int(input("Введите 1 число"))
D = int(input("Введите 2 число"))
B = []
for i in range(0, 10):
    B.append(A * D ** i)
print(B)