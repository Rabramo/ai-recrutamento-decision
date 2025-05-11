# Projeto Datathon POSTECH – Fase 5

## Descrição do Desafio

Este projeto foi desenvolvido como parte da Fase 5 do Datathon do curso de Data Analytics da POSTECH. O objetivo é propor uma solução baseada em Inteligência Artificial para otimizar o processo de recrutamento e seleção da empresa Decision, especializada em serviços de bodyshop para o setor de tecnologia da informação.

## Objetivo do Projeto

Desenvolver um MVP que utilize dados históricos da empresa para prever a compatibilidade entre candidatos e vagas com base nos seguintes critérios:

- Habilidades técnicas (como linguagens de programação)
- Aderência à cultura organizacional da contratante
- Grau de engajamento e motivação do candidato

## Estrutura do Projeto

- `dados/`: arquivos de dados brutos e tratados
- `notebooks/`: notebooks com análises exploratórias e testes
- `src/`: código-fonte principal para pré-processamento, modelagem e utilitários
- `app/`: aplicação desenvolvida em Streamlit
- `modelos/`: modelos treinados salvos no formato `.pkl`
- `testes/`: testes unitários (caso aplicável)
- `README.md`: documentação do projeto
- `requirements.txt`: lista de dependências do projeto

## Tecnologias Utilizadas

- Python 3.10
- pandas, numpy, matplotlib, seaborn
- scikit-learn
- streamlit
- joblib
- nltk
- spacy

## Instalação

Clone o repositório e instale os pacotes necessários com o seguinte comando:

```bash
pip install -r requirements.txt

### 📦 Acesso ao dataset tratado

O arquivo `prospeccao_consolidada.parquet` contém os dados integrados e normalizados a partir das fontes `candidatos.json`, `vagas.json` e `prospeccoes.json`.

> Tamanho aproximado: 130 MB  
> Acesso público via Google Drive

🔗 [Clique aqui para visualizar no Google Drive](https://drive.google.com/file/d/1eQ2TWeGqssR9ImxQw8y83xGl23_o4UN_/view?usp=sharing)

---

### 📥 Como carregar no Google Colab

```python
import pandas as pd

# Link direto para leitura do parquet
url = "https://drive.google.com/uc?id=1eQ2TWeGqssR9ImxQw8y83xGl23_o4UN_"

# Carregando com pyarrow
df = pd.read_parquet(url, engine='pyarrow')

# Visualizar amostra
df.head()
