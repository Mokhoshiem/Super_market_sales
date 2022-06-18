#!/usr/bin/env python
# coding: utf-8

# ## # Importing libraries

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# #### Importing data

# In[2]:


df = pd.read_csv("D:/data/supermarket_sales - Sheet1.csv")


# ### Data exploration

# In[3]:


df.head()


# In[4]:


df.describe()


# In[5]:


df.shape


# ### Observations:
# * There is no empty values
# * Data set has 1000 rows
# * Data set has 17 columns

# ### Geting duplicate values

# In[6]:


duplicate_values = df[df.duplicated()].count()


# In[7]:


duplicate_values


# #### No duplicates, Then searching for missing values:

# In[8]:


nan_values = df[df.isnull()].count()


# In[9]:


nan_values


# ### There is no missing values

# # Analysis:

# ### break into two data frames one for females and one for males

# In[10]:


#  males df
males_mask = df.Gender == "Male"
df_male = df[males_mask]
df_male


# In[11]:


# females df
female_mask = df.Gender == "Female"
df_female = df[female_mask]
df_female


# ## Males Vs. Females transactions

# In[166]:


genders = df.groupby('Gender')
dif_genders = genders['Invoice ID'].count()
dif_genders.plot(kind='bar')
plt.title('Males Vs. Females orders')
plt.show()
print(dif_genders)


# In[167]:


dif_sales = genders['Total'].sum()
dif_sales.plot(kind='pie')
plt.title('Females Vs. Males total sales')
plt.show()
print(dif_sales)


# In[168]:


# rating
ratings = genders['Rating'].mean()
ratings.plot(kind='bar')
plt.title('Males Vs. Females mean rating')
plt.show()
print(ratings)


# In[18]:


df.columns


# ## General behavior

# In[41]:


# sales by branch
branching = df.groupby('Branch')
# by city
city_categs = df.groupby('City')
# by product line
p_line_categs = df.groupby('Product line')


# ### Branch comparison

# In[119]:


sales_by_branch = branching['Total'].sum()
sales_by_branch.plot(kind='bar')
plt.title('Total sales by branch')
plt.ylabel('Total Sales')
plt.grid()
plt.show()
print(sales_by_branch)


# In[120]:


# Ratings by branch
rates = branching['Rating'].mean()
rates.plot(kind='bar')
plt.title('Rating by branch')
plt.ylabel('Rating')
plt.show()
print(rates)


# In[124]:


#  Gros income
gros_by_branch = branching['gross income'].sum()
gros_by_branch.plot(kind='bar')
plt.title('Gross income by branch')
plt.show()
print(gros_by_branch)


# In[ ]:





# In[169]:


# sales trend
sales_trend = df.groupby('Date')['Total'].sum()
sales_trend.plot(figsize=(15,7))
plt.title('Sales trend over time')


# In[101]:


# sales by product line
sales_by_p_line = p_line_categs['Total'].sum()
sales_by_p_line.plot(kind='bar')


# # Branch A

# In[48]:


branch_A = df[df['Branch']=='A']
branch_A.head()


# In[50]:


branch_a_by_product = branch_A.groupby('Product line')


# In[62]:


products_branch_a = branch_a_by_product['Total'].sum()
products_branch_a.plot(kind='bar')
plt.title('Total sales by product line in branch A')


# In[70]:


males_in_a = branch_A[branch_A['Gender']=='Male']
# print(males_in_a.head())
females_in_a = branch_A[branch_A['Gender']=='Female']
# print(females_in_a)


# In[156]:


# Sales trends by date
by_date_branch_a = branch_A.groupby('Date')
total_sales_by_date_branch_a = by_date_branch_a['Total'].sum()
total_sales_by_date_branch_a.plot(figsize=(15,7))


# In[155]:


orders_by_date_branch_a = by_date_branch_a['Total'].count()
orders_by_date_branch_a.plot(figsize=(15,5))


# ###  It's noticed that trend is up in the middle of months

# In[142]:


df['Date'].max()


# In[143]:


df['Date'].min()


# ## Studying males behavior

# ### Membership

# In[19]:


#  Number of males with and without membership
males_membership = df_male.groupby("Customer type")
male_members = males_membership["Invoice ID"].count()[0]
male_normals = males_membership["Invoice ID"].count()[1]


# In[20]:


# total purchase by males with and without membership
members_total = males_membership['Total'].sum()[0]
normals_total = males_membership['Total'].sum()[1]


# In[21]:


#  invoice drop size (ds) with and without membership
ds_members = males_membership['Total'].mean()[0]
ds_normals = males_membership['Total'].mean()[1]


# In[170]:


x = ['Members','Normals']
fig,(ax, ax1, ax2) = plt.subplots(nrows=1,ncols=3, figsize=(15,7))

# the count of members Vs. normals
ax.bar(x=x,height=[male_members,male_normals])
ax.set_title('Count')

# total purchse by members vs. normals
ax1.bar(x=x, height=[members_total, normals_total])
ax1.set_title('Total purchse')


# drp size
ax2.bar(x=x, height=[ds_members, ds_normals])
ax2.set_title('Drop size (ds)')

# plt.title('\t Memebers Vs. Normals\n')
# plt.legend()
plt.show()
print('Males Total sales\n',males_membership['Total'].sum())
print('\n\nMales Number of orders\n',males_membership['Invoice ID'].count())
print('\n\nMAles Invoice drop size\n',males_membership['Total'].mean())


# ### Payment methods

# In[175]:


payment_methods_males = df_male.groupby('Payment')


# In[178]:


# Orders by method
orders_by_payment = payment_methods_males['Invoice ID'].count()
orders_by_payment


# In[179]:


# total sales by method
males_total_sales_by_method = payment_methods_males['Total'].sum()
males_total_sales_by_method


# In[211]:


x = orders_by_payment.keys()
fig, (ax_1,ax_2) = plt.subplots(ncols=2,nrows=1,figsize=(12,5))
ax_1.bar(x=x,height=orders_by_payment)
ax_1.set_title('Males # Orders by payment method')

ax_2.pie(males_total_sales_by_method, labels=x)
ax_2.set_title('Males Total sales by payment method')
plt.show()
print('# orders by method\n', orders_by_payment)
print('\n\nTotal sales by method\n', males_total_sales_by_method)


# In[ ]:





# In[199]:




