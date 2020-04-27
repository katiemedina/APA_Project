# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 20:46:10 2020

@author: Katie
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pyplot import figure
#%%
df = pd.read_csv('rides_and_reliability.csv')

buses = df[['gtfs_route_id', 'pct_reliable', 'boardings', 'route_indicator']]

buses = buses.sort_values(['pct_reliable'], ascending = True)

buses = buses.reset_index()

#%%
#Reliability and Ridership
plt.figure(figsize=(12,8))
plt.subplots_adjust(hspace = 0.45)
sns.set(style='whitegrid')

#Reliability
plt.subplot(2,1,1)
sns.set(style = 'whitegrid')
fg1 = sns.barplot(x='gtfs_route_id', y="pct_reliable", data=buses, 
            order=buses.sort_values('pct_reliable').gtfs_route_id, color = 'salmon')
fg1.set(xlabel = 'Route ID', ylabel = 'Percent Reliable')
fg1.set_title('Reliability by Route')

#Ridership
plt.subplot(2,1,2)
fg2 = sns.barplot(x='gtfs_route_id', y="boardings", data=buses, order=buses.sort_values('boardings').gtfs_route_id, color = 'blue')
fg2.set(xlabel = 'Route ID', ylabel = 'Typical Boardings')
fg2.set_title('Boardings by Route')
plt.savefig('Reliability and Boardings by Route.png')

#%%

buses.plot(x = 'gtfs_route_id', kind= 'bar' , secondary_y= 'boardings' , rot= 0 , figsize = (12,6))
plt.savefig('ReliabilityxBoardings.png')

