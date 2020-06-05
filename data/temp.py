

#%%

import os
import pandas as pd

data = pd.read_csv('ContosoCoffee.csv')



# %%

import re
s = data['AddressLine'][0]

def convert_to_branch(address):
    result = None
    pattern = r'[a-zA-Z\s]+'
    words_only = re.search(pattern=pattern, string=address)
    if words_only:
        result = words_only[0].strip()
    if result:
        return f"{result} Branch"
    else:
        return ''

data['AddressLine'] = data['AddressLine'].apply(lambda x: convert_to_branch(x))

#%%

data[data['AddressLine']=='']

# %%

# Remove non_us, blank addresses
us_data = data[data['Country']=='US']
print(len(us_data))
us_data = us_data[data['AddressLine']!='']
print(len(us_data))
#%%
us_data['Branch_ID'] = [f"B-{1000+i}" for i in range(len(us_data))]

#%%

us_data.to_csv('ContosoCoffee.txt', sep='\t')

#%%

from collections import Counter
sorted(
    Counter(us_data.AdminDivision).items(),
    key = lambda x: x[1],
    reverse=True
)

#%%


