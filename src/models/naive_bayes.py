import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report, accuracy_score
import os
import time

data_path = os.path.join("..", "..", "data", "processed_data.csv")

print("Carregando dados...")
start_time = time.time()
data = pd.read_csv(data_path)
print(f"Dados carregados. Número de linhas: {len(data)}. Tempo: {time.time() - start_time:.2f} segundos.")

print("Criando a coluna 'liked'...")
start_time = time.time()
data['liked'] = (data['rating'] >= 4.0).astype(int)
print(f"Coluna 'liked' criada. Tempo: {time.time() - start_time:.2f} segundos.")

print("Selecionando as features e a variável alvo...")
start_time = time.time()
X = data.drop(columns=["liked", "userId", "movieId", "rating", "timestamp", "title"])  # Apenas 'genres' é mantida
y = data["liked"]
print(f"Features e variável alvo selecionadas. Tempo: {time.time() - start_time:.2f} segundos.")

print("Convertendo 'genres' para representação binária...")
start_time = time.time()
X = X['genres'].str.get_dummies('|')
print(f"Conversão concluída. Número de features após transformação: {X.shape[1]}. Tempo: {time.time() - start_time:.2f} segundos.")

print("Dividindo os dados em treino e teste...")
start_time = time.time()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Divisão concluída. Tamanho do conjunto de treino: {len(X_train)}. Tamanho do conjunto de teste: {len(X_test)}. Tempo: {time.time() - start_time:.2f} segundos.")

print("Treinando o modelo Naive Bayes...")
start_time = time.time()
model = GaussianNB()
model.fit(X_train, y_train)
print(f"Modelo treinado. Tempo: {time.time() - start_time:.2f} segundos.")

print("Fazendo previsões...")
start_time = time.time()
y_pred = model.predict(X_test)
print(f"Previsões concluídas. Tempo: {time.time() - start_time:.2f} segundos.")

print("Gerando relatório de desempenho...")
start_time = time.time()
report = classification_report(y_test, y_pred, target_names=["Não Gostei", "Gostei"])
accuracy = accuracy_score(y_test, y_pred)
print(f"Relatório gerado. Tempo: {time.time() - start_time:.2f} segundos.")

output_path = os.path.join("..", "..", "results", "naive_bayes_report.txt")
print(f"Salvando relatório em: {output_path}...")
start_time = time.time()
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, "w") as f:
    f.write("Relatório de Classificação - Naive Bayes\n")
    f.write(report)
    f.write(f"\nAcurácia: {accuracy:.2f}")
print(f"Relatório salvo. Tempo: {time.time() - start_time:.2f} segundos.")

print("Execução concluída.")
