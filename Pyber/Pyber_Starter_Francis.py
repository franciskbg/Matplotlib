
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[17]:


city_data= pd.read_csv("data/city_data.csv")
city_data.head()


# In[18]:


ride_data=  pd.read_csv("data/ride_data.csv")
ride_data.head()


# In[12]:


#Combine the data into a single dataset
merging_table = pd.merge(city_data, ride_data, on="city")


# In[21]:


# Combine the data into a single dataset
merging_table = merging_table[["city","date","fare","ride_id","driver_count","type"]]
merging_table.head(6)


# In[40]:


#obtaining the X and Y coordinates for each area. We'll start with the Urban city first

urban = merging_table .loc[merging_table ["type"] == "Urban",:]
urban_mean = urban.groupby(["city"]).mean()

urban_area_x = urban["city"].value_counts()
urban_area_y = urban_mean["fare"]
urban_area_d = urban_mean["driver_count"]

urban_axis = np.arange(0, len(urban), 1)


# In[41]:


#finding out the X & Y values for the rural area 
rural= merging_table.loc[merging_table["type"] == "Rural",:]
rural_mean = rural.groupby(["city"]).mean()

rural_area_x = rural["city"].value_counts()
rural_area_y = rural_mean["fare"]
rural_d = rural_mean["driver_count"]

rural_axis = np.arange(0, len(rural), 1)


# In[42]:


#find the valu for X and Y for the suburbs area
suburbs = merging_table.loc[merging_table["type"] == "Suburban",:]
suburbs_mean = suburbs.groupby(["city"]).mean()

suburban_area_x = suburbs["city"].value_counts()
suburban_area_y = suburbs_mean["fare"]
suburban_are_d = suburbs_mean["driver_count"]

suburban_axis = np.arange(0, len(suburbs), 1)

