import random

def Max(mas, leftMas, rightMas):
    if leftMas == rightMas:
        return mas[leftMas]

    mid = (leftMas + rightMas) // 2

    max_left = Max(mas, leftMas, mid)
    max_right = Max(mas, mid + 1, rightMas)
    if max_right > max_left:
        return max_right
    else:
        return max_left

try:
    mas = []
    count = int(input("Введите количество рандомных чисел: "))
    for i in range(1, count+1):
        mas.append(random.randint(-100, 100))
    n = len(mas)
    print(mas)
    print(f'Max: {Max(mas, 0, n - 1)}')
except ValueError:
    print('Введите корректные данные!')