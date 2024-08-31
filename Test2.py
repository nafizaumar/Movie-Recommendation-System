#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd


# In[10]:


# Load the datasets
movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')


# In[11]:


# Filter ratings for the specific movieId
terminator_ratings = ratings[ratings['movieId'] == terminator_id]


# In[13]:



# Calculate the average rating
average_rating = terminator_ratings['rating'].mean()

print(f'The average user rating for "Terminator 2: Judgment Day (1991)" is {average_rating:.2f}')

