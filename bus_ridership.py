# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 16:02:07 2020

@author: Katie
"""
import pandas as pd
import zipfile

#%%
zf = zipfile.ZipFile('MBTA_Bus_Ridership_by_Trip_Season_RouteLine_and_Stop.zip') 

#add low_memory = False to deal with mixed type column error
rides = pd.read_csv(zf.open('MBTA_Bus_Ridership_by_Trip_Season_RouteLine_and_Stop.csv'),low_memory=False)

bad_buses = pd.read_csv('bad_buses.csv')
#%%
#subset data to just Fall 2018 rides
is_2018 = rides['season'] == 'Fall 2018'

rides18 = rides[is_2018]

#%%
#GROUP BY LINE WITHOUT DIRECTION
glrides18 = rides18.groupby(['route_id'])

glrides18_sum = glrides18['boardings'].sum()

#%%
#add ridership numbers to bad buses identified in reliability data
bad_buses['str_route'] = bad_buses['gtfs_route_id'].astype(str)

bus_merged = bad_buses.merge(glrides18_sum,
                            how = 'left',
                            left_on = 'str_route',
                            right_on = 'route_id',
                            validate = '1:1',
                            indicator = True)

print('\n')
print(bus_merged['_merge'].value_counts())

bus_merged.drop(['_merge'], axis = 'columns', inplace = True)

bus_merged.to_csv('rides_and_reliability.csv')
