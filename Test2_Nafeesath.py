#!/usr/bin/env python
# coding: utf-8

# In[137]:


import pandas as pd


# In[140]:


# Load the datasets
movies_df = pd.read_csv('movies.csv')
ratings_df = pd.read_csv('ratings.csv')
ratings_df


# In[72]:



grouped_ratings = ratings_df.groupby('movieId').agg(
    count=('rating', 'count'), 
    mean=('rating', 'mean')
).reset_index()


# In[73]:


#Apply an inner join between movies.csv and the grouped dataframe
merged_df = pd.merge(movies_df, grouped_ratings, on='movieId', how='inner')


# In[74]:


#  Filter only those movies which have more than 50 user ratings
filtered_movies = merged_df[merged_df['count'] > 50]


# In[75]:


# result
print(filtered_movies.head())


# In[76]:



# Find the movie with the highest average user rating
most_popular_movie = filtered_movies.sort_values(by='mean', ascending=False).head(1)


# In[77]:


# Display the result
print(most_popular_movie[['title', 'mean']])


# In[78]:


# Find the top 5 most popular movies based on the number of user ratings
top_5_popular_movies = filtered_movies.sort_values(by='count', ascending=False).head(5)


# In[79]:


# Display the result
print(top_5_popular_movies[['title', 'count']])


# In[80]:


# Filter for Sci-Fi movies
sci_fi_movies = filtered_movies[filtered_movies['genres'].str.contains('Sci-Fi')]


# In[81]:


# Sort the filtered Sci-Fi movies by the number of user ratings
sci_fi_movies_sorted = sci_fi_movies.sort_values(by='count', ascending=False)


# In[82]:


# Get the third most popular Sci-Fi movie based on the number of user ratings
third_most_popular_sci_fi_movie = sci_fi_movies_sorted.iloc[2]  # third movie in sorted order


# In[83]:


# Display the result
print(third_most_popular_sci_fi_movie[['title', 'count']])


# In[102]:


import pandas as pd
import requests
from bs4 import BeautifulSoup


# In[103]:


# Load the datasets
movies_df = pd.read_csv('movies.csv')
ratings_df = pd.read_csv('ratings.csv')
links_df = pd.read_csv('links.csv')
 


# In[129]:


print(movies_df)


# In[104]:


# Step 1: Group the user ratings based on movieId and apply aggregation operations
grouped_ratings = ratings_df.groupby('movieId').agg(
    count=('rating', 'count'), 
    mean=('rating', 'mean')
).reset_index()


# In[105]:


# Step 2: Apply an inner join between movies.csv and the grouped dataframe
merged_df = pd.merge(movies_df, grouped_ratings, on='movieId', how='inner')


# In[106]:


# Step 3: Filter only those movies which have more than 50 user ratings
filtered_movies = merged_df[merged_df['count'] > 50]


# In[107]:


# Step 4: Merge filtered movies with IMDb links
filtered_movies = pd.merge(filtered_movies, links_df, on='movieId', how='inner')

# Display the first few rows of the filtered dataset with IMDb IDs
print(filtered_movies.head())


# In[118]:


# Function to scrape reviews from IMDb
def scrape_imdb_reviews(imdb_id):
    url = f'https://www.imdb.com/title/tt{imdb_id}/reviews'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract reviews
    reviews = []
    for review in soup.find_all('div', class_='text show-more__control'):
        reviews.append(review.get_text())

    return reviews


# In[125]:


# Example: Scrape reviews for the first movie in the filtered list
first_movie_id = str(filtered_movies['imdbId'].iloc[0]).zfill(7)  # Ensure IMDb ID is 7 digits
first_movie_title = filtered_movies['title'].iloc[0]

reviews = scrape_imdb_reviews(first_movie_id)

print(f"Reviews for '{first_movie_title}':")
print(reviews)


# In[85]:


# Load the original datasets
movies_df = pd.read_csv('movies.csv')
ratings_df = pd.read_csv('ratings.csv')
links_df = pd.read_csv('links.csv')


# In[86]:


# Step 1: Group the user ratings based on movieId and apply aggregation operations
grouped_ratings = ratings_df.groupby('movieId').agg(
    count=('rating', 'count'), 
    mean=('rating', 'mean')
).reset_index()


# In[87]:


# Step 2: Apply an inner join between movies.csv and the grouped dataframe
merged_df = pd.merge(movies_df, grouped_ratings, on='movieId', how='inner')


# In[88]:


# Step 3: Filter only those movies which have more than 50 user ratings
filtered_movies = merged_df[merged_df['count'] > 50]


# In[89]:


# Save the filtered DataFrame to CSV
filtered_movies.to_csv('filtered_movies.csv', index=False)


# In[90]:


# Now you can read it again if needed
filtered_movies = pd.read_csv('filtered_movies.csv')


# In[91]:


import pandas as pd
import requests
from bs4 import BeautifulSoup


# In[92]:


# Load the movies data (assuming `filtered_movies` DataFrame is available)
filtered_movies = pd.read_csv('filtered_movies.csv')
links_df = pd.read_csv('links.csv')


# In[93]:


# Merge the filtered movies with their IMDb links using 'movieId'
merged_data = pd.merge(filtered_movies, links_df, on='movieId')


# In[94]:


# Function to scrape reviews from IMDb
def scrape_imdb_reviews(imdb_id):
    url = f'https://www.imdb.com/title/tt{imdb_id}/reviews'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract reviews
    reviews = []
    for review in soup.find_all('div', class_='text show-more__control'):
        reviews.append(review.get_text())

    return reviews

# Scrape reviews for each movie with more than 50 ratings
all_reviews = {}
for index, row in merged_data.iterrows():
    imdb_id = str(row['imdbId']).zfill(7)  # Ensure the IMDb ID is 7 digits long
    movie_title = row['title']
    reviews = scrape_imdb_reviews(imdb_id)
    all_reviews[movie_title] = reviews



# In[95]:


# Example output for verification
print(all_reviews)


# In[96]:


import pandas as pd

# Load the original datasets
movies_df = pd.read_csv('movies.csv')
ratings_df = pd.read_csv('ratings.csv')
links_df = pd.read_csv('links.csv')


# In[97]:


# Step 1: Group the user ratings based on movieId and apply aggregation operations
grouped_ratings = ratings_df.groupby('movieId').agg(
    count=('rating', 'count'), 
    mean=('rating', 'mean')
).reset_index()


# In[98]:


# Step 2: Apply an inner join between movies.csv and the grouped dataframe
merged_df = pd.merge(movies_df, grouped_ratings, on='movieId', how='inner')


# In[99]:


# Step 3: Filter only those movies which have more than 50 user ratings
filtered_movies = merged_df[merged_df['count'] > 50]


# In[100]:


# Save the filtered DataFrame to CSV
filtered_movies.to_csv('filtered_movies.csv', index=False)
print("Filtered movies data has been saved to 'filtered_movies.csv'.")

# Now read it back to confirm
filtered_movies = pd.read_csv('filtered_movies.csv')
print(f"Read filtered movies data with shape: {filtered_movies.shape}")

# Display the first few rows to confirm


# In[101]:


print(filtered_movies.head())


# In[ ]:





# In[ ]:





# In[ ]:




