# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 20:46:10 2020

@author: Katie
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#%%
df = pd.read_csv('rides_and_reliability.csv')

buses = df[['gtfs_route_id', 'pct_reliable', 'boardings', 'route_indicator']]

buses = buses.sort_values(['pct_reliable'], ascending = True)

buses = buses.reset_index()

#%%

plt.figure()
sns.set(style = 'whitegrid')
fig1 = sns.barplot(data = buses, x = 'gtfs_route_id', y = 'pct_reliable')


#%%
#PLOT BEST AND WORST RELIABLE
#NEED TO SORT PROPERLY SO DISPLAY LOWEST TO HIGHEST
plt.subplots_adjust(hspace = 0.45)
sns.set(style='whitegrid')
plt.subplot(2,1,1)
fg1 = sns.barplot(x = 'gtfs_route_id', y = 'pct_reliable', data=buses, color = 'salmon')
fg1.set_ylim([0,100])
fg1.set_title("Reliability")
fg1.set(xlabel = 'Route ID', ylabel = 'Percentage On Time')

plt.subplot(2,1,2)
fg2 = sns.barplot(x = 'gtfs_route_id', y = 'boardings', data=buses, color = 'green')
fg2.set_title("Ridership")
fg2.set(xlabel = 'Route ID', ylabel = 'Typical Boardings')



#ax = sns.barplot(x = 'gtfs_route_id', y = 'pct_reliable', data = reliability2018, hue = 'peak_offpeak_ind')

#%%

fig = plt.figure()
ax = fig.add_subplot(111)
ax2 = ax.twinx()

width = 0.4
buses.pct_reliable.plot(kind = 'bar', color = 'red', ax = ax, width = width, position = 1)
buses.boardings.plot(kind = 'bar', color = 'blue', ax = ax2, width = width, position = 0)

plt.show()

#%%
buses.plot(x = 'gtfs_route_id', kind= 'bar' , secondary_y= 'boardings' , rot= 0 )
plt.show()

