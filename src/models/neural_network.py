import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from keras.models import Sequential
from keras.layers import Dense
import os

data_path = os.path.join("..", "..", "data", "processed_data.csv")

print("Carregando dados...")
data = pd.read_csv(data_path)

data['liked'] = (data['rating'] >= 4.0).astype(int)

X = data.drop(columns=["liked", "userId", "movieId", "rating", "timestamp", "title"]) 
y = data["liked"]

X = X['genres'].str.get_dummies('|')

print("Dividindo os dados em treino e teste...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Construindo o modelo de Rede Neural...")
model = Sequential()
model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

print("Treinando o modelo de Rede Neural...")
model.fit(X_train, y_train, epochs=10, batch_size=64, verbose=1)

print("Avaliando o modelo...")
y_pred = (model.predict(X_test) > 0.5).astype(int)

print("Gerando relatório de desempenho...")
report = classification_report(y_test, y_pred, target_names=["Não Gostei", "Gostei"])
accuracy = accuracy_score(y_test, y_pred)

output_path = os.path.join("..", "..", "results", "neural_network_report.txt")
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, "w") as f:
    f.write("Relatório de Classificação - Rede Neural\n")
    f.write(report)
    f.write(f"\nAcurácia: {accuracy:.2f}")

print("Relatório salvo em:", output_path)
