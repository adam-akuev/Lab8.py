def SortDec3(A, B, C):
    Mas = [A, B, C]
    for i in range(1, 3):
        if Mas[1] < Mas[0]:
            Mas[0], Mas[1] = Mas[1], Mas[0]
        if Mas[1] > Mas[2]:
            Mas[1], Mas[2] = Mas[2], Mas[1]
    return Mas

try:
    for i in range(2):
        A1 = float(input('Введите значение A:'))
        B1 = float(input('Введите значение B:'))
        C1 = float(input('Введите значение C:'))
        CCC = SortDec3(A1, B1, C1)
        print(CCC)
except ValueError:
    print('Введите корректные данные!!!')