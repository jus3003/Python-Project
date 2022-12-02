#1. Create Function to Pull From Database and clean data for specific materials
#2. Create Function that takes a request for specific material and pulls E value for that material

import requests
import numpy as np
import pandas as pd

#Extract Elastic Modulus

#Use inputs as seen on the website table
#examples
#getE('ABS plastics')
#getE('Aluminum')
#getE('Concrete')

def getE(Material):

    #Get Data from the website and store in Data Frame
    url = 'https://www.engineeringtoolbox.com/young-modulus-d_417.html'
    html = requests.get(url).content
    df_list = pd.read_html(html)
    df = df_list[-1]
    df.to_csv('MaterialProperties.csv')
    df.columns = ['Material', 'YM', 'UTS', 'YS']

    #Create dictionary to associate materials with their E values
    data = df.to_dict(orient='index')
    
    #Search the dictionary for the getE() input material
    i = Material
    n = 0
    for n in range(len(data)):
        #when material is found store the Young's Modulus
        if i == data[n]['Material']:
            Epull = data[n]['YM']
        else:
            n = n + 1
        
    #Check if no E value is given in table
    if Epull == 'NaN':
        print("There is no Young's Modulus Available")
    #Check if a range is given and return the lowest E value
    else:
        E = (float(Epull.split('-')[0])*(10**6)) #Convert GPa to Pa
        print("The Young's Modulus is ",E," Pa")


#Extract price history of materials (Note: we could graph these on mat plotlib and output graph on our GUI to show user how the price of metals are going)

url = 'https://www.bls.gov/regions/mid-atlantic/data/producerpriceindexmetals_us_table.htm'
html = requests.get(url).content
df_list = pd.read_html(html)
df = df_list[-1]
print(df)
df.to_csv('MaterialCosts.csv')
