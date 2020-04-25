# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 23:58:26 2020

@author: Katie
"""

import pandas as pd
import matplotlib as plt
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
#MONTHLY TOTALS KEY BUSES
#ALL FOLLOWING ANALYSIS IS FOR KEY BUSES; NEED TO DO WITH REGULAR BUS ROUTES
key_buses['year'] = key_buses['year+month'].dt.year

#group by route, peak or off peak, and year+month
kgroute_month = key_buses.groupby(['gtfs_route_id','peak_offpeak_ind','year+month'])

#apply sum to columns after grouped by object is created
kgroute_month_sum = kgroute_month[['otp_numerator','otp_denomi_tor']].sum()

#adds percentage reliability column
kgroute_month_sum['pct_reliable'] = round((kgroute_month_sum ['otp_numerator']/kgroute_month_sum ['otp_denomi_tor'])*100,2).copy()

#turns multi-index back into columns in dataframe
test = kgroute_month_sum.reset_index()

#%%
#group and calculate by year
test['year'] = test['year+month'].dt.year

test_year_peak = test.groupby(['year','peak_offpeak_ind','gtfs_route_id'])

test_year_peak_sum = test_year_peak[['otp_numerator','otp_denomi_tor']].sum()

test_year_peak_sum['pct_reliable'] = round((test_year_peak_sum['otp_numerator']/test_year_peak_sum['otp_denomi_tor'])*100,2)

test_year_peak_sum = test_year_peak_sum.sort_values(['gtfs_route_id','peak_offpeak_ind','year'])

#%%
#2018
test_year_peak_sum = test_year_peak_sum.reset_index()

year2018buses = test_year_peak_sum['year'] == 2018

reliability2018 = test_year_peak_sum[year2018buses]
#look at offpeak
is_peak = reliability2018['peak_offpeak_ind'] == 'PEAK'

reliability2018peak = reliability2018[is_peak]

#%%

ax = sns.barplot(x = 'gtfs_route_id', y = 'pct_reliable', data = reliability2018, hue = 'peak_offpeak_ind')
