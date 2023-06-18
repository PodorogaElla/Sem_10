from math import *
from sympy import *
from sympy.plotting import plot
import numpy as np
import pandas as pd
from scipy import *
from matplotlib import *
from matplotlib import pyplot as plt
from sklearn import *
import scipy.stats as stats

foot = np.array([173, 175, 180, 178, 177, 185, 183, 182])
hoсk = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
weight = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])
print (stats.shapiro(foot))
print (stats.shapiro(hoсk))
print (stats.shapiro(weight))
print (stats.bartlett(foot,hoсk,weight))
print (stats.f_oneway(foot,hoсk,weight))
print (stats.kruskal(foot,hoсk,weight))
from statsmodels.stats.multicomp import pairwise_tukeyhsd

data = pd.DataFrame({'group': ['foot']*8 + ['hoсk']*9 + ['weight']*11,
                     'height': [173, 175, 180, 178, 177, 185, 183, 182,
                                177, 179, 180, 188, 177, 172, 171, 184, 180,
                                172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170]})
print (data)
tukey = pairwise_tukeyhsd(data["height"], data["group"], alpha = 0.05)
print(tukey)