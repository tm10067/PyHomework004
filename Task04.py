# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от-100 до 100) многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем 
# данную итерацию степени
# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0



def construct_equation():
    k = int(input("введите степень уравнения: "))
    from random import randint
    eq = ''
    for i in range(k, -1, -1):
        c = randint(-100, 100)
        if c > 1:
            if i == k:
                eq += str(c) + 'X^' + str(i)
            else:
                eq += ' + ' + str(c) + 'X^' + str(i)
        elif c < -1: 
            if i == k:
                eq += '-' + str(abs(c)) + 'X^' + str(i)
            else:
                eq += ' - ' + str(abs(c)) + 'X^' + str(i)
        elif c == 0:
            continue
    eq = eq.replace('X^1', 'X').replace('X^0', '').replace('-1X', '-X').replace(' 1X', ' X') + ' = 0'
    return eq

with open(r'Task04.txt', 'w') as data:
    data.write(construct_equation())
    data.close()
