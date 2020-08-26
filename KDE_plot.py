#KDE plot
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
from scipy.stats import zscore
import seaborn as sns
sns.set(color_codes=True)
plt.figure(num=None, figsize=(12, 9), dpi=80, facecolor='w', edgecolor='k')

plt.rc('font', size=210)          # controls default text sizes
plt.rc('axes', titlesize=10)     # fontsize of the axes title
plt.rc('axes', labelsize=10)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=8)    # fontsize of the tick labels
plt.rc('ytick', labelsize=10)    # fontsize of the tick labels
plt.rc('legend', fontsize=10)    # legend fontsize
plt.rc('figure', titlesize=10)  # fontsize of the figure title



df = pd.read_csv('Turbo293_mean_log2.csv')
df.head()
myplot = sns.kdeplot(df.Turbo_mean)
myplot = sns.kdeplot(df.Lysis_mean)
plt.show()
