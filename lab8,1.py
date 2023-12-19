import random

def RAST(x, y, TRI):
    min_distance = float()

    for i in range(len(TRI)):
        x1, y1 = TRI[i]
        x2, y2 = TRI[(i+1) % len(TRI)]
        S = ((y2 - y1) * x - (x2 - x1) * y + x2 * y1 - x1 * y2) / ((x2 - x1)**2 + (y2 - y1)**2) ** (0.5) #Уравнение расстояния между вершиной и точкой
        if S < min_distance:
            min_distance = S
    if min_distance < 0:
        min_distance = min_distance * (-1)

    return (min_distance)

try:
    TRI = []
    for i in range(3):
        Ver1 = (random.randint(0, 15), random.randint(0, 15))
        TRI.append(Ver1)
    x = float(input('Введите координаты точки X: '))
    y = float(input('Введите координаты точки Y: '))
    S = RAST(x, y, TRI)
    print(TRI)
    print(S)
except ValueError:
    print('Введите корректные данные!')