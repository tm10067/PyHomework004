# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0
# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0

import codecs

source1 = codecs.open(r'Task05source1.txt', 'r', "utf-8")
x = source1.read()
source1.close()

source2 = codecs.open(r'Task05source2.txt', 'r', "utf-8")
y = source2.read()
source2.close()

def equation_to_dict(x):
    x = str(x).replace('⁰', "0").replace('¹', "1").replace('²', "2").replace('³', "3").replace('⁴', "4").replace('⁵', "5").replace('⁶', "6").replace('⁷', "7").replace('⁸',"8").replace('⁹', "9")
    list_x = x.replace("+ ", "").replace(" - ", " -").replace(" x", " 1x").replace(" = 0", "x0").split(" ")
    dict_x = {}
    for i in list_x:
        dict_x[int(i.split("x")[1])] = int(i.split("x")[0])
    return dict_x

dict_x = equation_to_dict(x)
dict_y = equation_to_dict(y)

def sum_dict_values (dict_x, dict_y):
    list_z = (dict_x, dict_y)
    dict_z = {}
    for i in list_z:
        for j in i.keys():
            dict_z[j] = dict_z.get(j, 0) + i[j]
    dict_z = dict(sorted(dict_z.items(), reverse = True))
    return (dict_z)
    
dict_z = sum_dict_values(dict_x, dict_y)

def dict_to_equation(dict_x):
    list_x = []
    for i in dict_x:
        k = str(dict_x[i]) + 'x^' + str(i)
        list_x.append(k)
    x = ' + '.join(list_x) + " = 0"
    x = x.replace('+ -',"-").replace(" -", " - ").replace("x^1", "x").replace("x^0", "").replace(" 1x", " x").replace("-1x", "-x")
    x = x.replace('^2', "²").replace('^3', "³").replace('^4', "⁴").replace('^5', "⁵").replace('^6', "⁶").replace('^7', "⁷").replace('^8',"⁸").replace('^9', "⁹")   
    return x
    
z = dict_to_equation(dict_z)

print(z)

data = codecs.open(r'Task05result.txt', 'w', "utf-8")
data.write(z)
data.close()