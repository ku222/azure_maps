
#%%
import pandas as pd
import os

# %%

csv_name = 'ContosoCoffee'
df = pd.read_csv(f"{csv_name}.csv")


#%%

test_txt = df.to_csv('text_tsv.txt', sep='\t')
