#!/usr/bin/env python
# coding: utf-8

# In[45]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sales = pd.read_csv('Amazon Sale Report.csv')


# In[8]:


sales.shape


# In[9]:


sales.describe()


# In[10]:


sales.info


# In[13]:


sales.head()


# In[14]:


sales.tail()


# In[15]:


sales.info()


# In[ ]:


# Data Cleaning


# In[46]:


# Drop Unrelated / black Columns

sales.drop(['New' , 'PendingS'], axis = 1, inplace =True)


# In[17]:


sales.info()


# In[18]:


# Check Null Values
pd.isnull(sales)


# In[20]:


# Sum will Give Total Values of Null Values
pd.isnull(sales).sum()


# In[21]:


sales.shape


# In[23]:


#  Drop null Values
sales.dropna(inplace =True)


# In[24]:


sales.shape


# In[25]:


sales.columns


# In[26]:


sales.info()


# In[27]:


# Change Data type 

sales['ship-postal-code'] = sales['ship-postal-code'].astype('int')


# In[28]:


# Checking whether the data type or not

sales['ship-postal-code'].dtype


# In[30]:


#  To change the date type of date columns (object to date)
sales['Date'] = pd.to_datetime(sales['Date'])


# In[34]:


sales['Date'].dtype


# In[35]:


sales.info()


# In[37]:


#  Rename the Column
sales.rename(columns={'Qty':'Quantity'})


# In[38]:


# Describe() method return description of the data in the DateFrame(i.e count,mean , std,min ...etc)
sales.describe()


# In[39]:


#  if you need to apply a describe method on object column data type the used include keyword
sales.describe(include = 'object')


# In[43]:


# if you need to apply any specified column then 
sales[['Qty','Amount']].describe()


# In[48]:


# Exploratory Data Analysis


# In[49]:


sales.columns


# In[50]:


# Size

ax =sns.countplot(x = 'Size' , data = sales)


# In[54]:


# give label on the bar graphs
ax = sns.countplot(x='Size' , data= sales)
for bars in ax.containers:
    ax.bar_label(bars)


# In[56]:


# Note : From Above the graph we can see that most of the people buys M-size


# In[57]:


#  Group By 
# The grooupby() function in pandas is used to group data based on one or more columns in a dataFrame


# In[59]:


sales.groupby(['Size'],as_index = False)['Qty'].sum().sort_values(by ='Qty',ascending =False)


# In[64]:


sales_Qty = sales.groupby(['Size'], as_index = False)['Qty'].sum().sort_values(by='Qty',ascending=False)
sns.barplot(x='Size',y = 'Qty',data =sales_Qty)


# In[65]:


#  Note : From above Graph we can see that most of the Qunatity buy m -size in the sales


# In[66]:


# Courier Status


# In[67]:


sns.countplot(data = sales , x = 'Courier Status' , hue ='Status')


# In[72]:


plt.figure(figsize = (9,5))
ax=sns.countplot(data =sales,x ='Courier Status',hue ='Status')


# In[73]:


# Note : from above the graph the majority of the orders are shipped through the courier


# In[74]:


# Histogram Diagram 


# In[77]:


sales['Size'].hist()


# In[81]:


# Catogory
sales['Category'] = sales['Category'].astype(str)
column_data = sales['Category']
plt.figure(figsize=(10,5))
plt.hist(column_data,bins = 30 , edgecolor = 'Black')
plt.xticks(rotation = 90)
plt.show()


# In[84]:


# note  : from above Gragh you can see that most of the buyers are buy T-shirt


# In[91]:


# Check B2B Data By using pie Chart

b2b_sales = sales['B2B'].value_counts()

plt.pie(b2b_sales, labels =b2b_sales.index, autopct ='%1.1f%%')
plt.show()


# In[92]:


#  Note : From Above the chart we can see the maximum i.e 99.3% of the buyer are retailers and 0.8% are B2b buyers


# In[93]:


#  Scatter plot


# In[94]:


x_data = sales['Category']
y_data = sales['Size']

plt.scatter(x_data , y_data)
plt.xlabel('Category')
plt.ylabel('Size')
plt.title('Scatter plot')
plt.show()


# In[100]:


# plot count of cities by state

plt.figure(figsize =(15,6))
sns.countplot(data = sales,x ='ship-state')
plt.xlabel('ship-state')
plt.ylabel('count')
plt.title('Distribution of state')
plt.xticks(rotation =90)
plt.show()


# In[102]:


# top 10 state 
top_state = sales['ship-state'].value_counts().head(10)
plt.figure(figsize=(12,6))
sns.countplot(data =sales[sales['ship-state'].isin(top_state.index)],x = 'ship-state')
plt.xlabel('ship-state')
plt.ylabel('count')
plt.title('Distrubution of state')
plt.xticks(rotation = 90)
plt.show()


# In[103]:


#  Note from above Graph we can see that most of the buyers from the maharashtra state


# In[104]:


# # Conclusion

# the data analysis reveals that the business has a siginficant customer base in maharshtra state mainly serves retailer , fulfills order through 
# amazone , exoeriences high demand for T-shirt and size is M-size as the preferred choice among buyers


# In[ ]:




