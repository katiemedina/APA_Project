# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 15:47:31 2020

@author: Katie
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 11:43:25 2020

@author: Katie
"""

import requests
import pandas as pd

#%%
var_string = 'NAME,B00001_001E'

#%%
api = 'https://api.census.gov/data/2018/acs/acs5'

for_clause = 'tract:*'

in_clause = 'state:25'

key_value = '5b0174d265e13d8cb4d448fe44c5e4981678a3be'

payload = {'get':var_string, 
           'for': for_clause, 
           'in': in_clause, 
           'key': key_value}

response = requests.get(api, payload)

if response.status_code == 200:
    print('\n', 'Request Succeeded')
else:
        print('\n', response.status_code)
        print(response.text)
        assert False

#%%
row_list = response.json()

colnames = row_list[0]

datarows = row_list[1:]

results = pd.DataFrame(columns = colnames, data = datarows)

results['geoid'] = results['state'] + results['county'] + results['tract']

results['pop_int'] = results['B00001_001E']

results.set_index('geoid', inplace = True)

newnames = {'B20002_001E' : 'median'}

results.rename(newnames, axis = 'columns', inplace = True)

results.to_csv('pop_by_tract.csv')