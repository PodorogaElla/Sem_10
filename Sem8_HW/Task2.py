import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt


x = np.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111])
n = x.size
alpha = 0.05
print( f'Среднее арифметическое = {np.mean( x ):.4f}' )
print( f'Среднее квадратичное отклонение = {np.std(x,ddof=1):.4f}' )
print( f'Несмещенная Дисперсия = {np.var( x, ddof=1 ):.4f}' )
print( f'Стандартное отклонение = {np.var( x, ddof=1 )**0.5:.4f}' )

# t = stats.t.ppf(1 - alpha / 2, n - 1)
# d = (t * np.std) / ((n) ** 0.5)
# d,t
# mean = x.mean()
# min = mean - d
# max = mean + d
# print(f'>>> Доверительный интервал для математического ожидания с '
#       f'надежностью 0.95 составляет:{min: .2f};{max: .2f}')