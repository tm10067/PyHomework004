# Вычислить число c заданной точностью *d*
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001

import math
import decimal

precise = int(input("введите количество знаков после запятой: ")) 
if precise > 10:
    precise = 10
elif precise < 1:
    precise = 1
d = decimal.Decimal(1) / decimal.Decimal(10 ** precise) 
pi = decimal.Decimal(math.pi)
print(pi)
print(f"при d = {d}, pi = {pi.quantize(d, rounding = decimal.ROUND_DOWN)}")
