import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
import os

os.makedirs('../../outputs/models', exist_ok=True)

data = pd.read_csv('../../data/processed_data.csv')

X = data.drop(['rating', 'userId', 'movieId', 'title', 'genres'], axis=1)
y = (data['rating'] >= 4).astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier(max_depth=10, random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
report = classification_report(y_test, predictions)

with open('../../outputs/models/decision_tree_report.txt', 'w') as f:
    f.write(report)

print("Relatório salvo em '../../outputs/models/decision_tree_report.txt'")
