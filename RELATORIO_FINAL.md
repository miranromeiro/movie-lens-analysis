
---

# **Relatório de Análise de Modelos de IA**

Este relatório contém os resultados de três modelos de classificação usados para prever se um usuário gostou ou não de um filme, com base em dados de avaliações de filmes. Os modelos treinados são: **Árvore de Decisão**, **Naive Bayes** e **Rede Neural**. A seguir, apresentamos os resultados detalhados de cada modelo, seguidos de um comparativo final.

## **1. Árvore de Decisão**

A Árvore de Decisão foi treinada para prever a probabilidade de um usuário gostar de um filme com base nas características dos dados. A seguir estão os resultados obtidos:

### **Matriz de Desempenho:**

```
              precision    recall  f1-score   support
           0       0.54      0.48      0.51   3382120
           1       0.53      0.59      0.56   3384313

    accuracy                           0.53   6766433
   macro avg       0.53      0.53      0.53   6766433
weighted avg       0.53      0.53      0.53   6766433
```

**Insights:**
- O modelo apresenta uma **acurácia de 53%**, com um equilíbrio entre as classes.
- A precisão para a classe 1 (Gostei) é um pouco melhor que para a classe 0 (Não Gostei), o que pode indicar que o modelo tem mais facilidade em classificar os filmes como "Gostei".
- A **recall** para a classe 1 (Gostei) é maior, mostrando que o modelo tem maior capacidade de identificar quando um filme foi bem avaliado.

---

## **2. Naive Bayes**

O modelo de **Naive Bayes** foi utilizado para realizar a mesma classificação. Este modelo assume independência entre as variáveis e foi treinado para prever se um usuário gostou de um filme.

### **Matriz de Desempenho:**

```
Relatório de Classificação - Naive Bayes
              precision    recall  f1-score   support

  Não Gostei       0.53      0.80      0.64   3382120
      Gostei       0.59      0.29      0.39   3384313

    accuracy                           0.55   6766433
   macro avg       0.56      0.55      0.51   6766433
weighted avg       0.56      0.55      0.51   6766433

Acurácia: 0.55
```

**Insights:**
- A **acurácia** do modelo é de 55%, levemente superior ao modelo de Árvore de Decisão.
- O modelo tem um desempenho muito bom para a classe "Não Gostei", com uma recall de 0.80, mas a precisão e recall para a classe "Gostei" são significativamente mais baixos, o que sugere que o modelo tem dificuldades em classificar corretamente os filmes como "Gostei".
- **F1-Score** para a classe "Não Gostei" (0.64) é bem mais alto do que para a classe "Gostei" (0.39), refletindo um desbalanceamento na capacidade de previsão entre as duas classes.

---

## **3. Rede Neural**

A **Rede Neural** foi construída usando a Keras API, com camadas densas e ativação **ReLU** para as camadas ocultas e **sigmoide** para a camada de saída. A seguir estão os resultados:

### **Matriz de Desempenho:**

```
Relatório de Classificação - Rede Neural
              precision    recall  f1-score   support

    Não Gostei       0.53      0.51      0.52   3382120
    Gostei           0.54      0.56      0.55   3384313

    accuracy                           0.53   6766433
   macro avg       0.53      0.53      0.53   6766433
weighted avg       0.53      0.53      0.53   6766433
```

**Insights:**
- O modelo de **rede neural** obteve uma **acurácia de 53%**, semelhante à Árvore de Decisão, mas não apresentou uma melhoria significativa.
- A **precisão** e **recall** são muito próximas entre as duas classes, mostrando um equilíbrio no desempenho do modelo.
- O modelo possui um desempenho razoável, mas poderia ser melhorado com mais camadas e neurônios.

---

## **4. Comparativo Final entre os Modelos**

| Modelo             | Acurácia | F1-Score (0) | F1-Score (1) |
|--------------------|----------|--------------|--------------|
| **Árvore de Decisão**  | 53%      | 0.51         | 0.56         |
| **Naive Bayes**        | 55%      | 0.64         | 0.39         |
| **Rede Neural**        | 53%      | 0.52         | 0.55         |

### **Discussão:**
- **Naive Bayes** teve a melhor acurácia, mas sua performance foi desbalanceada, com a classe "Gostei" sendo mais difícil de prever. Este modelo teve um bom desempenho para a classe "Não Gostei", mas sua utilidade é limitada pela baixa precisão na classificação de filmes "Gostei".
- **Árvore de Decisão** mostrou-se equilibrada, mas com precisão e recall similares entre as classes, o que reflete uma distribuição mais balanceada dos dados.
- **Rede Neural** não apresentou grandes melhorias, com desempenho semelhante à Árvore de Decisão. No entanto, sua flexibilidade pode permitir melhorias com mais ajustes nas camadas e nos hiperparâmetros.

### **Possíveis melhorias:**
- Para o **Naive Bayes**, seria interessante explorar outras representações dos dados, talvez com mais características para reduzir a dependência de uma única variável (como "genres").
- O modelo de **Rede Neural** pode ser melhorado adicionando mais camadas e ajustando os hiperparâmetros para obter uma maior capacidade de generalização.
- A **Árvore de Decisão** pode ser refinada com técnicas de poda para evitar o overfitting e melhorar a generalização.

---
