import pandas as pd

print("Iniciando o pré-processamento...")

try:
    movies = pd.read_csv('../data/movies.csv')
    ratings = pd.read_csv('../data/ratings.csv')
    print("Arquivos CSV carregados com sucesso.")
except Exception as e:
    print(f"Erro ao carregar arquivos: {e}")
    exit()

print(f"Filmes: {movies.shape}, Avaliações: {ratings.shape}")

processed_data = pd.merge(ratings, movies, on='movieId', how='inner')
print(f"Dados processados: {processed_data.shape}")

output_path = '../data/processed_data.csv'
try:
    processed_data.to_csv(output_path, index=False)
    print(f"Arquivo salvo com sucesso em: {output_path}")
except Exception as e:
    print(f"Erro ao salvar o arquivo: {e}")
