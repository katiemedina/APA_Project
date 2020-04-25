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

#%%
#subset data to just Fall 2018 rides
is_2018 = rides['season'] == 'Fall 2018'

rides18 = rides[is_2018]

#%%
#BY DIRECTION
group_line_rides18 = rides18.groupby(['route_id','direction_id'])

group_line_rides18_sum = group_line_rides18['boardings'].sum()

test = group_line_rides18_sum.unstack()

test = test.reset_index()

test['approx_annual_0'] = test[0]*52

test['approx_annual_0'] = test[1]*52

#%%
#WITHOUT DIRECTION
glrides18 = rides18.groupby(['route_id'])

glrides18_sum = glrides18['boardings'].sum()


