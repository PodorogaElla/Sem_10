import numpy as np
import pandas as pd
from scipy.stats import  binom
from scipy.stats import  poisson

def combinations(n, k):
    return (np.math.factorial(n)/(np.math.factorial(k)*np.math.factorial(n-k)))

#===========================HomeWork-3==================================

#1. Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
# Посчитать (желательно без использования статистических методов наподобие std, var, mean) среднее арифметическое,
# среднее квадратичное отклонение, смещенную и несмещенную оценки дисперсий для данной выборки.

sal = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])
#считаем среднее арифметическое
sa=sal.sum()/sal.size
sa_=sal.mean()

#создаём массив квадратов разности
saq=(sal-sa)**2
#считаем СКО
std=(saq.sum()/sal.size)**.5
stdd=(saq.sum()/(sal.size-1))**.5

std_=sal.std()
stdd_=sal.std(ddof=1)

#считаем дисперсию смещенная оценка
var=saq.sum()/sal.size
var_=sal.var()

#считаем дисперсию несмещенная оценка
vard=saq.sum()/(sal.size-1)
vard_=sal.var(ddof=1)

print("1. Среднее арифметическое ",sa,sa_)
print("1. СКО ",std,std_)
print("1. дисперсия смещенная оценка ",var,var_)
print("1. дисперсия несмещенная оценка ",vard,vard_)

