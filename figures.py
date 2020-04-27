# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 20:46:10 2020

@author: Katie
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#%%
buses = pd.read_csv('rides_and_reliability.csv')

buses = buses.sort_values(['pct_reliable'], ascending = True)

buses = buses.reset_index(drop = True)

#%%
#PLOT BEST AND WORST RELIABLE
#NEED TO SORT PROPERLY SO DISPLAY LOWEST TO HIGHEST
plt.subplots_adjust(hspace = 0.45)
sns.set(style='whitegrid')
plt.subplot(2,1,1)
fg1 = sns.barplot('str_route', 'pct_reliable', data=buses)
fg1.set_ylim([0,100])
fg1.set_title("Reliability")
fg1.set(xlabel = 'Route ID', ylabel = 'Percentage On Time')

plt.subplot(2,1,2)
fg21 = sns.barplot('str_route', 'boardings', data=buses)
fg2.set_title("Ridership")
fg2.set(xlabel = 'Route ID', ylabel = 'Typical Boardings')
