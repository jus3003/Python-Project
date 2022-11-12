#1. Create Function to Pull From Database and clean data for specific materials
#2. Create Function that takes a request for specific material and pulls E value for that material

import requests
import numpy as np
import pandas as pd

#Extract Elastic Modulus

url = 'https://www.engineeringtoolbox.com/young-modulus-d_417.html'
html = requests.get(url, verify = False)
df_list = pd.read_html(html)
df = df_list[-1]
print(df)
df.to_csv('MaterialProperties.csv')


#Extract price history of materials (Note: we could graph these on mat plotlib and output graph on our GUI to show user how the price of metals are going)

url = 'https://www.bls.gov/regions/mid-atlantic/data/producerpriceindexmetals_us_table.htm'
html = requests.get(url).content
df_list = pd.read_html(html)
df = df_list[-1]
print(df)
df.to_csv('MaterialCosts.csv')