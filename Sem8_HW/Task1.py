import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
plt.scatter(zp,ks)

plt.xlabel ('Величина заработной платы "ZP"')
plt.xlabel ('Поведенческий кредитный скоринг "KS"', rotation=90)
plt.show()

cov_zp_ks = np.mean(zp*ks) - np.mean(zp)*np.mean(ks)
print (cov_zp_ks)

corr = cov_zp_ks / (np.std(zp) * np.std(ks))
print (corr)

corr_coef = cov_zp_ks / (np.std(zp, ddof=0) * np.std(ks, ddof=0))
print (corr_coef)
#numpy
corr_numpy = np.corrcoef(zp, ks)[0][1]
print (corr_numpy)
#pandas
corr_pandas = pd.Series(zp).corr(pd.Series(ks), method='pearson')
print (corr_pandas)