#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import json , requests
from bs4 import BeautifulSoup
df = pd.read_csv('destinations_LP_crawler_Ex5.csv',encoding='latin-1')
df1 = pd.DataFrame(df['city'])
df1['city'][22] = 'malopolska/krakow'
df1['city'][35] = 'dodecanese/kos'


# In[2]:


KEY = ('KEY')
response = []
for c in df1['city']:
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s' % (c,KEY)
    response.append(requests.get(url).json())


# In[3]:


list0 = []
for keys in response:
    list0.append(keys['results'][0]['formatted_address'])


# In[4]:


list1 = []
for country in list0:
    try:
        int(country.split(",")[-1])
        list1.append(country.split(",")[-2])
    except:
        list1.append(country.split(",")[-1])        
df1['country'] = list1
df1['city'][22] = 'krakow'
df1['city'][35] = 'kos'
list4 = []


# In[5]:


for k in range(0,len(df1['city'])):
    url2 = "https://www.lonelyplanet.com/"+df1.iloc[k]['country'].strip()+"/"+df.iloc[k]['city_LP']
    html = requests.get(url2)
    soup = BeautifulSoup(html.text,'html.parser')
    par = soup.find('div' , attrs={"class":'readMore_content___5EuR'})
    tags = par.find('p').get_text()
    list4.append(tags)
df1['Description'] = list4

 
    


# In[10]:


df1.to_csv('LP_destinations.csv',index=False)

