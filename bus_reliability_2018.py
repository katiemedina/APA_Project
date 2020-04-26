# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 18:16:32 2020

@author: Katie
"""

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

#%%
#subset dataset into bus and key bus only
is_buses = mbta['mode_type'] == 'Bus'

is_key = (mbta['route_category'] == 'Key Bus') or (mbta['route_category'] == 'Silver Line')

not_key = mbta['route_category'] == 'Other Bus'

buses = mbta[is_buses].copy()

key_buses = buses[is_key].copy()

not_key_buses = buses[not_key].copy()

#%%
#ANNUAL TOTALS - NOT KEY BUSES
#group by route, peak or off peak, and year+month
groute = not_key_buses.groupby(['gtfs_route_id','peak_offpeak_ind','year'])

#apply sum to columns after grouped by object is created
groute_sum = groute[['otp_numerator','otp_denomi_tor']].sum()

#adds percentage reliability column
groute_sum['pct_reliable'] = round((groute_sum ['otp_numerator']/groute_sum ['otp_denomi_tor'])*100,2)

#turns multi-index back into columns in dataframe
groute_sum = groute_sum.reset_index()

#%%
#2018
year2018 = groute_sum['year'] == 2018

reliability2018 = groute_sum[year2018]

is_peak = reliability2018['peak_offpeak_ind'] == 'PEAK'

peak_reliability2018 = reliability2018[is_peak]

worst_peak_reliability2018 = peak_reliability2018.sort_values(['pct_reliable'])[0:15]

list_worst = worst_peak_reliability2018['gtfs_route_id']
print(list_worst)

best_peak_reliability2018 = peak_reliability2018.sort_values(['pct_reliable'])[-10:]

worst_peak_reliability2018['route_indicator'] = 'not key'

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
#ANNUAL TOTALS - KEY BUSES
#group by route, peak or off peak, and year+month
kgroute = key_buses.groupby(['gtfs_route_id','peak_offpeak_ind','year'])

#apply sum to columns after grouped by object is created
kgroute_sum = kgroute[['otp_numerator','otp_denomi_tor']].sum()

#adds percentage reliability column
kgroute_sum['pct_reliable'] = round((kgroute_sum ['otp_numerator']/kgroute_sum ['otp_denomi_tor'])*100,2)

#turns multi-index back into columns in dataframe
kgroute_sum = kgroute_sum.reset_index()

#%%
#2018 KEY ROUTES
kyear2018buses = kgroute_sum['year'] == 2018

kreliability2018 = kgroute_sum[kyear2018buses]

kis_peak = kreliability2018['peak_offpeak_ind'] == 'PEAK'

kpeak_reliability2018 = kreliability2018[kis_peak].copy()

kpeak_reliability2018['route_indicator'] = 'key'

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

#%%
#COMBINED LIST OF BAD ROUTES
bad_buses = kpeak_reliability2018.append(worst_peak_reliability2018, ignore_index = True)

bad_buses['map_route_id'] = bad_buses['gtfs_route_id'].str.zfill(2)

bad_buses.to_csv('bad_buses.csv')
