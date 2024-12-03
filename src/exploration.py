import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

os.makedirs('../outputs/exploration', exist_ok=True)

movies = pd.read_csv('../data/movies.csv')
ratings = pd.read_csv('../data/ratings.csv')

sns.histplot(ratings['rating'], bins=10, kde=True)
plt.title('Distribuição de Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequência')
plt.savefig('../outputs/exploration/rating_distribution.png')
plt.clf()

movies['genres'] = movies['genres'].str.split('|')
all_genres = [genre for genres in movies['genres'] for genre in genres]
genre_counts = pd.Series(all_genres).value_counts()

sns.barplot(x=genre_counts.index, y=genre_counts.values)
plt.title('Gêneros Mais Populares')
plt.xticks(rotation=45)
plt.savefig('../outputs/exploration/popular_genres.png')
plt.clf()
