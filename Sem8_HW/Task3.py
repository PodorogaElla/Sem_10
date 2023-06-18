import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

var = 25
n = 27
mean = 174.2
std = (var)**0.5
alpha = 0.05
z=stats.norm.ppf(1-alpha/2,n-1)
d=z*std/(n)**0.5
min = mean - d
max = mean + d
print(f'>>> Доверительный интервал для математического ожидания с надежностью 0.95 '
      f'составляет' f':{min: .2f};{max: .2f}')