# Projeto de Análise de Dados de Filmes

Este projeto realiza a análise e classificação de filmes com base nas avaliações dos usuários utilizando modelos de IA. Os modelos treinados incluem **Árvore de Decisão**, **Naive Bayes** e **Rede Neural**. Abaixo, você encontrará as instruções para executar o projeto na sua máquina.

## Requisitos

- Python 3.7 ou superior
- Bibliotecas Python: pandas, scikit-learn, numpy, keras, entre outras.

## Estrutura de Pastas

```
movie-lens-analysis/
├── data/
│   ├── processed_data.csv        # Arquivo CSV com os dados processados (necessário para execução)
├── results/                      # Pasta onde os relatórios de resultados serão salvos
├── src/                          
│   ├── models/                   
│   │   ├── decision_tree.py      # Script do modelo de Árvore de Decisão
│   │   ├── naive_bayes.py        # Script do modelo Naive Bayes
│   │   ├── neural_network.py     # Script do modelo de Rede Neural
│   ├── preprocessing.py          # Script para pré-processamento dos dados
├── requirements.txt              # Lista de dependências
├── README.md                     # Este arquivo
```

## Passos para Execução

### 1. Clone o repositório

Primeiramente, faça o clone do repositório para sua máquina local:

```bash
git clone <URL_DO_REPOSITORIO>
cd movie-lens-analysis
```

### 2. Crie um Ambiente Virtual

Recomenda-se o uso de um ambiente virtual para isolar as dependências do projeto:

```bash
python -m venv venv
```

### 3. Ative o Ambiente Virtual

- No Windows:

```bash
venv\Scripts\activate
```

- No Linux/MacOS:

```bash
source venv/bin/activate
```

### 4. Instale as Dependências

Instale todas as dependências necessárias listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 5. Carregue os Arquivos CSV

Para rodar o projeto, é necessário que os seguintes arquivos CSV estejam presentes na pasta **`data`**:

- **`movies.csv`**: Contém informações sobre os filmes (ID, título, gêneros, etc.).
- **`ratings.csv`**: Contém as avaliações dos usuários para os filmes.

Além disso, se você precisar processar os dados, o arquivo **`processed_data.csv`** será gerado na pasta **`data`** após rodar o script de pré-processamento.


### 6. Pré-processamento dos Dados

Se você ainda não tem o arquivo **`processed_data.csv`**, você pode processar os dados utilizando o script **`preprocessing.py`**. Para isso, execute o seguinte comando:

```bash
python src/preprocessing.py
```

Isso irá gerar o arquivo **`processed_data.csv`** na pasta **`data`**.

### 7. Executando os Modelos

Agora, você pode rodar os scripts de treinamento para cada modelo:

#### Árvore de Decisão:

```bash
python src/models/decision_tree.py
```

#### Naive Bayes:

```bash
python src/models/naive_bayes.py
```

#### Rede Neural:

```bash
python src/models/neural_network.py
```

Cada um desses scripts irá treinar o respectivo modelo e gerar um relatório de desempenho na pasta **`results`**.

### 8. Verificando os Resultados

Os relatórios dos modelos treinados serão salvos automaticamente na pasta **`results`**. O relatório contém métricas como **precisão**, **recall**, **F1-score** e **acurácia**.

Os relatórios são salvos no formato `.txt` com o nome do modelo.

## Considerações Finais

- Certifique-se de que o arquivo **`processed_data.csv`** esteja presente na pasta **`data`** antes de rodar os scripts de treinamento.