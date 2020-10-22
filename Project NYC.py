#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
### import libraries
import numpy as np
import pandas as pd


import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns


# In[2]:


service311 = pd.read_csv (r'C:\Users\Milind\Desktop\Business Analyst\LVC\Python\Python for Data Science\311_Service_Requests_from_2010_to_Present.csv')


# In[3]:


service311.head()


# In[4]:


service311.shape


# In[5]:


service311.columns


# In[7]:


service311['Complaint Type'].unique()


# In[8]:


service311['Descriptor'].unique()


# In[9]:



complaintTypecity = pd.DataFrame({'count':
                                  service311.groupby(['Complaint Type','City']).size()}).reset_index()
complaintTypecity


# In[10]:


service311.groupby(['Borough','Complaint Type','Descriptor']).size()


# In[11]:


import datetime


# In[13]:


df = pd.read_csv(r'C:\Users\Milind\Desktop\Business Analyst\LVC\Python\Python for Data Science\311_Service_Requests_from_2010_to_Present.csv', parse_dates=["Created Date", "Closed Date"])


# In[14]:


df["Request_Closing_Time"] = df["Closed Date"] - df["Created Date"]


# In[15]:


#Have a look at the status of tickets
df['Status'].value_counts().plot(kind='bar',alpha=0.6,figsize=(7,7))
plt.show()


# In[16]:


#Complaint type Breakdown with bar plot to figure out majority of complaint types and top 10 complaints
service311['Complaint Type'].value_counts().head(10).plot(kind='barh',figsize=(5,5));


# In[17]:


service311.groupby(["Borough","Complaint Type","Descriptor"]).size()


# In[18]:


majorcomplints=service311.dropna(subset=["Complaint Type"])
majorcomplints=service311.groupby("Complaint Type")

sortedComplaintType = majorcomplints.size().sort_values(ascending = False)
sortedComplaintType = sortedComplaintType.to_frame('count').reset_index()

sortedComplaintType
sortedComplaintType.head(10)


# In[19]:


sortedComplaintType = sortedComplaintType.head()
plt.figure(figsize=(5,5))
plt.pie(sortedComplaintType['count'],labels=sortedComplaintType["Complaint Type"], autopct="%1.1f%%")
plt.show()


# In[20]:


#Group dataset by complaint type to display plot against city
groupedby_complainttype = df.groupby('Complaint Type')


# In[21]:


grp_data = groupedby_complainttype.get_group('Blocked Driveway')
grp_data.shape


# In[22]:


#To get nan values in the entire dataset
df.isnull().sum()


# In[23]:


#fix blank values in City column
df['City'].dropna(inplace=True)


# In[24]:


#Shape after dropping nan values
df['City'].shape


# In[25]:


#count of null values in grouped city column data
grp_data['City'].isnull().sum()


# In[26]:


#fix those NAN with "unknown city" value instead
grp_data['City'].fillna('Unknown City', inplace =True)


# In[27]:


#Scatter plot displaying all the cities that raised complaint of type 'Blocked Driveway'
plt.figure(figsize=(20, 15))
plt.scatter(grp_data['Complaint Type'],grp_data['City'])
plt.title('Plot showing list of cities that raised complaint of type Blocked Driveway')
plt.show()


# In[ ]:




