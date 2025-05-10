import pandas as pd

def preprocessamento_data(df):
    # Exemplo de tratamento simples
    df = df.copy()
    df.dropna(inplace=True)
    df['linguagem'] = df['linguagem'].map({
        "Python": 0, "Java": 1, "JavaScript": 2, "Outros": 3
    })
    return df
