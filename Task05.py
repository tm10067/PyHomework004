# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0
# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0

def construct_equation():
    from random import randint
    k = int(input("введите степень уравнения: "))
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
    eq = eq + ' = 0'
    return eq

def construct_dict(eq):
    eq_dict = {}
    eq = eq.replace(' + ', ' +').replace(' - ', ' -').split()[:-2]
    for i in range(len(eq)):
        eq[i] = eq[i].replace('+', '').split("X^")
        eq_dict[int(eq[i][1])] = int(eq[i][0])
    return eq_dict

eq1 = construct_equation()
eq_dict1 = construct_dict(eq1)
print(eq1)
print(eq_dict1)
eq2 = construct_equation()
eq_dict2 = construct_dict(eq2)
print(eq2)
print(eq_dict2)

for j in range()



# with open(r'Task04.txt', 'w') as data:
#     data.write(construct_equation(N))
#     data.close()