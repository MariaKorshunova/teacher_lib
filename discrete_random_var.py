"""Найдите математическое ожидание M(x), дисперсию D(x)
 и среднее квадратическое отклонение σ(X),
 если закон распределения случайно величины задан таблицей {2 rows, 5 column}
 Постройте многоугольник распределения случайно величины X"""

import random
import pandas as pd

def define_random_value_x():
    x1 = random.randrange(-5, 0, 1)
    x2 = random.randrange(0, 5, 1)
    x3 = random.randrange(5, 10, 1)
    x4 = random.randrange(10, 15, 1)
    return x1, x2, x3, x4

def define_random_value_p():
    p1 = random.randrange(1, 4, 1) / 10
    p2 = random.randrange(1, 4, 1) / 10
    p3 = random.randrange(1, 4, 1) / 10
    return p1, p2, p3

x1, x2, x3, x4 = define_random_value_x()
p1, p2, p3 = define_random_value_p()

# Задать величины вручную
# x1, x2, x3, x4 = 130, 140, 160, 180
# p1, p2, p3 = 0.05, 0.10, 0.25

p4 = 1 - p1 - p2 - p3
rows = ['X', 'p']
distribution_law = pd.DataFrame([[x1, x2, x3, x4], [p1, p2, p3, p4 ]], 
    index = rows)
E_x = round(x1*p1 + x2*p2 + x3*p3 + x4*p4, 2)
D_x = round((x1**2)*p1 + (x2**2)*p2 + (x3**2)*p3 + (x4**2)*p4 - E_x**2, 2)
Stdev = round(pow(D_x, 0.5), 2)
print('Distribution_law:')
print(distribution_law)
print('Математическое ожидание M(X)=', E_x)
print('Дисперсия D(X)=', D_x)
print('Cреднее квадратическое отклонение σ(X)=', Stdev)