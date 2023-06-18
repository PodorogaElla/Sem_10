import numpy as np
import matplotlib.pyplot as plt
def mse(b, x, y):
    return np.sum((b * x - y) ** 2) / len(x)
mse(b, zp, ks)

def mse_p(b,x,y):
    return (2 / len(x)) * np.sum((b * x - y) * x)
alpha = 1e-6
b = 0.1
mse_min = mse(b, zp, ks)
i_min = 1
b_min = b
iteration = 10000
for i in range(iteration):
    b -= alpha * mse_p(b, zp, ks)
    if i % 100 == 0:
        print(f'>>> Итерация #{i}, b={b}, mse={mse(b, zp, ks)}')
    if mse(b, zp, ks) > mse_min:
        print(f'>>> Итерация #{i_min}, b={b_min}, mse={mse_min},\n>>> Достигнут минимум\n>>> Получили {b_min} ')
        break
    else:
        mse_min = mse(b,zp,ks)
        i_min = i
        b_min = b