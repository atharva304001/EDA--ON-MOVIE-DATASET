#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[12]:


df=pd.read_csv("movies.csv")


# In[13]:


df


# In[14]:


df.info()


# # there are no missing/null values.

# In[15]:


df.describe()


# # deleting the columns which are not needed in EDA process.
# 

# In[17]:


column_list = ['popularity','homepage','id','imdb_id','keywords','overview','production_companies','vote_count','vote_average','budget_adj', 'revenue_adj']


df.drop(column_list, axis = 1, inplace = True)

df.head(3)


# In[19]:


df.drop_duplicates(keep='first' , inplace =True)


# In[21]:


df.shape


# # removed all the duplicate values from data
# 

# In[23]:


col = ['budget','revenue']
df[col] = df[col].replace(0, np.NaN)
df.dropna(subset = col, inplace = True)


# In[24]:


df


# In[27]:


df.dtypes


# In[29]:


df.release_date = pd.to_datetime(df['release_date'])


# In[30]:


df


# In[ ]:


change_type = ['budget','revenue']
df[change_type] = [change_type].astype('int64')


# # considering only integer part of data and elemenating decimal points.

# In[31]:


df.shape


# In[35]:





# # 1) Which are the movies with the third-lowest and third-highest budget?
# 

# In[38]:


high_revenue=df.sort_values(['budget'],ascending=False)
low_revenue=df.sort_values(['budget'],ascending=True)


# In[39]:


high_revenue


# # answer: 3rd highest movie is

# In[43]:


high_revenue.iloc[2][2]


# #  answer: 3rd lowest movie is
# 

# In[42]:


low_revenue.iloc[2][2]


# # 2) What is the average number of words in movie titles between the years 2000-2005?
# 

# In[49]:


title=df[(df['release_year'] >=2000) & (df['release_year'] <=2005)]
words=[]
for i in  title['original_title']:
    for j in i.split(' '):
        words.append(j)
print(len(words))        


# In[50]:


title.shape


# In[55]:


average_words=len(words)/785
average_words


# # 3) Which are the movies with the most and least earned revenue?
# 

# In[57]:


high_revenue_movie=df.sort_values(['revenue'],ascending=False)
low_revenue_movie=df.sort_values(['revenue'],ascending=True)


# # answer for movie with most earned revenue

# In[62]:


high_revenue_movie.iloc[0][2]


# # answer for movie with least earned revenue

# In[65]:


low_revenue_movie.iloc[0][2]


# # 4) What is the average runtime of movies in the year 2006?
#  

# In[73]:


run_time=df[df['release_year']==2006]
run_time.shape


# # average runtime is 

# In[79]:


average_runtime=df['runtime'].mean()
average_runtime

