import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração para exibir todos os resultados
pd.set_option('display.max_columns', None)

# Removida a linha problemática: plt.style.use('seaborn')

# Carregando apenas os dados necessários
ratings_df = pd.read_csv('ratings.csv')
movies_df = pd.read_csv('movies.csv')

def analyze_ratings():
    print("\n=== Análise de Ratings ===")
    print(f"Total de avaliações: {len(ratings_df)}")
    print(f"Total de usuários únicos: {ratings_df['userId'].nunique()}")
    print(f"Total de filmes avaliados: {ratings_df['movieId'].nunique()}")
    print("\nEstatísticas dos ratings:")
    print(ratings_df['rating'].describe())
    
    # Distribuição de ratings
    plt.figure(figsize=(10, 6))
    sns.histplot(ratings_df['rating'], bins=10)
    plt.title('Distribuição de Ratings')
    plt.xlabel('Rating')
    plt.ylabel('Contagem')
    plt.show()
    
    # Top 10 usuários mais ativos
    user_activity = ratings_df['userId'].value_counts().head(10)
    print("\nTop 10 usuários mais ativos:")
    print(user_activity)

def analyze_movies():
    # Separar gêneros
    genres_expanded = movies_df['genres'].str.get_dummies('|')
    
    print("\n=== Análise de Filmes e Gêneros ===")
    print(f"Total de filmes: {len(movies_df)}")
    print("\nContagem de filmes por gênero:")
    print(genres_expanded.sum().sort_values(ascending=False))
    
    # Média de ratings por gênero
    movie_ratings = ratings_df.merge(movies_df, on='movieId')
    genres_ratings = []
    
    for genre in genres_expanded.columns:
        genre_movies = movies_df[movies_df['genres'].str.contains(genre)]
        genre_ratings = ratings_df[ratings_df['movieId'].isin(genre_movies['movieId'])]
        genres_ratings.append({
            'genre': genre,
            'avg_rating': genre_ratings['rating'].mean(),
            'count': len(genre_ratings)
        })
    
    genres_df = pd.DataFrame(genres_ratings)
    genres_df = genres_df.sort_values('count', ascending=False)
    
    # Plotar média de ratings por gênero
    plt.figure(figsize=(12, 6))
    sns.barplot(data=genres_df, x='genre', y='avg_rating')
    plt.xticks(rotation=45)
    plt.title('Média de Ratings por Gênero')
    plt.tight_layout()
    plt.show()
    
    # Top 10 filmes mais avaliados
    top_movies = movie_ratings.groupby(['movieId', 'title'])['rating'].agg(['count', 'mean']).sort_values('count', ascending=False).head(10)
    print("\nTop 10 filmes mais avaliados:")
    print(top_movies)

def prepare_data_for_modeling():
    """Prepara os dados para a próxima fase de modelagem"""
    
    # Merge ratings com movies
    full_data = ratings_df.merge(movies_df, on='movieId')
    
    # Criar feature binária para classificação (rating alto/baixo)
    # Considerando ratings >= 4 como "alto"
    full_data['high_rating'] = (full_data['rating'] >= 4).astype(int)
    
    # One-hot encoding para gêneros
    genres_dummies = full_data['genres'].str.get_dummies('|')
    
    # Combinar dados
    modeling_data = pd.concat([full_data[['userId', 'movieId', 'rating', 'high_rating']], 
                             genres_dummies], axis=1)
    
    # Salvar para próxima fase
    modeling_data.to_csv('prepared_data.csv', index=False)
    print("\nDados preparados e salvos em 'prepared_data.csv'")

def main():
    analyze_ratings()
    analyze_movies()
    prepare_data_for_modeling()

if __name__ == "__main__":
    main()