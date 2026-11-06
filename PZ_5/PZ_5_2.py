# Описать функцию RectPS, вычисляющую периметр P и площадь S прямоугольника
# со сторонами, параллельными осям координат, по координатам (x1, y1), (x2, y2)
# его противоположных вершин. С помощью этой функции найти периметры и площади
# трех прямоугольников с данными противоположными вершинами.

reg = 3


def rect_ps(x1, y1, x2, y2):
    """Вернуть периметр и площадь прямоугольника по двум его вершинам."""
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    perimeter = 2 * (width + height)
    area = width * height
    return perimeter, area


def input_float(pro):
    """Запрашивать ввод, пока пользователь не введет вещественное число."""
    while True:
        try:
            return float(input(pro))
        except ValueError:  # обработка исключений
            print("Неправильно ввели! Нужно вещественное число.")


for number in range(1, reg + 1):
    print(f"Прямоугольник № {number}")
    x_1 = input_float("Введите x1: ")
    y_1 = input_float("Введите y1: ")
    x_2 = input_float("Введите x2: ")
    y_2 = input_float("Введите y2: ")

    p, s = rect_ps(x_1, y_1, x_2, y_2)
    print(f"Периметр P = {p}, площадь S = {s}")
