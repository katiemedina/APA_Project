# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 23:58:26 2020

@author: Katie
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#%%
mbta = pd.read_csv('MBTA_Commuter_Rail_Bus__Rapid_Transit_Reliability.csv', index_col = 'ObjectId')

#%%
#convert date to datetime format
mbta['date'] = pd.to_datetime(mbta['service_date'], format = '%Y/%m/%d')

#create year column
mbta['year'] = mbta['date'].dt.year

#create month column
mbta['month'] = mbta['date'].dt.month

#create year+month column to aggregate monthly totals
mbta['year+month'] = pd.to_datetime(mbta['year'].astype(str) + "/" + mbta['month'].astype(str))

#%%
#subset dataset into bus and key bus only
is_buses = mbta['mode_type'] == 'Bus'

is_key = mbta['route_category'] == 'Key Bus'

buses = mbta[is_buses]

key_buses = buses[is_key]

#%%
#MONTHLY TOTALS - ALL BUSES
#ALL FOLLOWING ANALYSIS IS FOR KEY BUSES; NEED TO DO WITH REGULAR BUS ROUTES
buses['year'] = buses['year+month'].dt.year

#group by route, peak or off peak, and year+month
groute_month = buses.groupby(['gtfs_route_id','peak_offpeak_ind','year+month'])

#apply sum to columns after grouped by object is created
groute_month_sum = groute_month[['otp_numerator','otp_denomi_tor']].sum()

#adds percentage reliability column
groute_month_sum['pct_reliable'] = round((groute_month_sum ['otp_numerator']/groute_month_sum ['otp_denomi_tor'])*100,2)

#turns multi-index back into columns in dataframe
g_route_month_sum = groute_month_sum.reset_index()

#%%
#group and calculate by year
g_route_month_sum['year'] = g_route_month_sum['year+month'].dt.year

g_route_year_peak = g_route_month_sum.groupby(['year','peak_offpeak_ind','gtfs_route_id'])

g_route_peak_sum = g_route_year_peak[['otp_numerator','otp_denomi_tor']].sum()

g_route_peak_sum['pct_reliable'] = round((g_route_peak_sum['otp_numerator']/g_route_peak_sum['otp_denomi_tor'])*100,2)

g_route_peak_sum = g_route_peak_sum.sort_values(['gtfs_route_id','peak_offpeak_ind','year'])

#%%
#2018
g_route_peak_sum = g_route_peak_sum.reset_index()

year2018buses = g_route_peak_sum['year'] == 2018

reliability2018 = g_route_peak_sum[year2018buses]

is_peak = reliability2018['peak_offpeak_ind'] == 'PEAK'

peak_reliability2018 = reliability2018[is_peak]

worst_peak_reliability2018 = peak_reliability2018.sort_values(['pct_reliable'])[0:10]

list_worst = worst_peak_reliability2018['gtfs_route_id']
print(list_worst)

best_peak_reliability2018 = peak_reliability2018.sort_values(['pct_reliable'])[-10:]

#%%
#PLOT BEST AND WORST RELIABLE
#NEED TO SORT PROPERLY SO DISPLAY LOWEST TO HIGHEST
plt.subplots_adjust(hspace = 0.45)
sns.set(style='whitegrid')
plt.subplot(2,1,1)
fg1 = sns.barplot(y='pct_reliable', x='gtfs_route_id',data=worst_peak_reliability2018, color = 'orange')
fg1.set_ylim([0,100])
fg1.set_title("Worst Reliability")
fg1.set(xlabel = 'Route ID', ylabel = 'Percentage On Time')

plt.subplot(2,1,2)
fg2 = sns.barplot(y='pct_reliable', x='gtfs_route_id',data=best_peak_reliability2018, color = 'green')
fg2.set_title("Best Reliability")
fg2.set(xlabel = 'Route ID', ylabel = 'Percentage On Time')
plt.savefig('stack_reliable.png')


#ax = sns.barplot(x = 'gtfs_route_id', y = 'pct_reliable', data = reliability2018, hue = 'peak_offpeak_ind')

#%%
#MONTHLY TOTALS - KEY BUSES
key_buses['year'] = key_buses['year+month'].dt.year

#group by route, peak or off peak, and year+month
kgroute_month = key_buses.groupby(['gtfs_route_id','peak_offpeak_ind','year+month'])

#apply sum to columns after grouped by object is created
kgroute_month_sum = kgroute_month[['otp_numerator','otp_denomi_tor']].sum()

#adds percentage reliability column
kgroute_month_sum['pct_reliable'] = round((kgroute_month_sum ['otp_numerator']/kgroute_month_sum ['otp_denomi_tor'])*100,2)

#turns multi-index back into columns in dataframe
kg_route_month_sum = kgroute_month_sum.reset_index()

#%%
#group and calculate by year
kg_route_month_sum['year'] = kg_route_month_sum['year+month'].dt.year

kg_route_year_peak = kg_route_month_sum.groupby(['year','peak_offpeak_ind','gtfs_route_id'])

kg_route_peak_sum = kg_route_year_peak[['otp_numerator','otp_denomi_tor']].sum()

kg_route_peak_sum['pct_reliable'] = round((kg_route_peak_sum['otp_numerator']/kg_route_peak_sum['otp_denomi_tor'])*100,2)

kg_route_peak_sum = kg_route_peak_sum.sort_values(['gtfs_route_id','peak_offpeak_ind','year'])


#%%
#2018 KEY ROUTES
kg_route_peak_sum = kg_route_peak_sum.reset_index()

kyear2018buses = kg_route_peak_sum['year'] == 2018

kreliability2018 = kg_route_peak_sum[year2018buses]

kis_peak = kreliability2018['peak_offpeak_ind'] == 'PEAK'

kpeak_reliability2018 = kreliability2018[kis_peak]

kworst_peak_reliability2018 = kpeak_reliability2018.sort_values(['pct_reliable'])[0:5]

klist_worst = kworst_peak_reliability2018['gtfs_route_id']
print(klist_worst)


#%%
#PLOT KEY ROUTE RELIABILITY
#NEED TO SORT PROPERLY TO DISPLAY LOWEST TO HIGHEST
plt.figure()
sns.set(style='whitegrid')
fg = sns.barplot(y='pct_reliable', x='gtfs_route_id',data=kpeak_reliability2018, color = 'orange')
fg.set_ylim([0,100])
fg.set_title("Reliability of Key Bus Routes")
fg.set(xlabel = 'Route ID', ylabel = 'Percentage On Time')
plt.savefig('stack_reliable_key.png')