#%% Importações

# Importações padrão
import os
import time
import warnings
import json

# Importações de terceiros
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("Dependências carregadas com sucesso!")
#%% Configurações globais

# Ignorar warnings
warnings.filterwarnings("ignore")

# Configurações do pandas
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', '{:.2f}'.format)
pd.set_option('display.precision', 2)

print("Configurações do pandas aplicadas com sucesso!")
#%% Estilo de Gráficos
# Configurações de estilo para gráficos
# Definindo o estilo padrão do matplotlib

# Resetando estilo para o padrão
# Para garantir que o estilo seja aplicado corretamente
plt.style.use('default')

# Definindo o estilo de gráfico
# Paleta inspirada em Storytelling with Data C. Nussbaumer Knaflic
# Usar cores neutras para contexto e ênfase para destaques
# Define o ciclo de cores para as séries de dados (linhas, barras, etc.)
# Usará azul escuro e laranja vivo alternadamente, seguindo a paleta de destaque de Knaflic
CORES = {
    "contexto": "#D3D3D3",      # cinza claro
    "destaque_azul": "#1f77b4", # azul escuro (similar ao padrão Matplotlib)
    "destaque_laranja": "#ff7f0e" # laranja vivo
}

plt.rcParams['axes.prop_cycle'] = plt.cycler(color=[CORES["destaque_azul"], CORES["destaque_laranja"]])
# Define a cor de fundo da área de plotagem como cinza claro (neutro)
# Isso suaviza o gráfico e tira o foco do fundo, realçando os dados
plt.rcParams['axes.facecolor'] = CORES["contexto"]
# Define a cor da borda dos eixos (X e Y) como cinza claro também
# Isso garante que as bordas não se destaquem mais que os dados
plt.rcParams['axes.edgecolor'] = CORES["contexto"]
plt.rcParams.update({
    'figure.figsize': (12, 6),
    'axes.titlesize': 16,
    'axes.labelsize': 14,
    'axes.labelweight': 'bold',
    'axes.titleweight': 'bold',
    'axes.titlepad': 10,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.spines.left': True,
    'axes.spines.bottom': True,
    'axes.grid': False,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'legend.frameon': False,
    'legend.fontsize': 12,
    'lines.linewidth': 2,
    'lines.markersize': 6,
    'font.family': 'sans-serif',
    'font.sans-serif': ['Calibri', 'Arial', 'DejaVu Sans']
})

print("Configurações de estilo aplicadas com sucesso!")
#%%
projeto = "/Users/rogerioabramoalvespretti/ai-recrutamento-decision/"

arquivos = {
    "vagas": projeto + "dados/brutos/vagas.json",
    "prospeccoes": projeto + "dados/brutos/prospeccoes.json",
    "candidatos": projeto + "dados/brutos/candidatos.json"
}

def carregar_dados(caminhos: dict) -> dict:
    """
    Carrega arquivos JSON estruturados em um dicionário de DataFrames.
    Para arquivos com chaves como IDs (ex: '31000'), transforma essas chaves em colunas.

    Parâmetros:
        caminhos (dict): dicionário com nomes e caminhos dos arquivos.

    Retorno:
        dict: dicionário com chave -> DataFrame correspondente.
    """
    dados = {}


    for chave, caminho in caminhos.items():
        if os.path.isfile(caminho):
            try:
                with open(caminho, encoding="utf-8") as f:
                    conteudo = json.load(f)

                    # Se for um dicionário com IDs (e valores também dicionários)
                    if isinstance(conteudo, dict) and all(isinstance(v, dict) for v in conteudo.values()):
                        lista_com_id = [{"id": k, **v} for k, v in conteudo.items()]
                        df = pd.json_normalize(lista_com_id, sep=".")
                        dados[chave] = df
                    elif isinstance(conteudo, list):
                        df = pd.json_normalize(conteudo, sep=".")
                        dados[chave] = df
                    else:
                        print(f"[AVISO] Estrutura inesperada no arquivo '{chave}'. Tentando converter diretamente.")
                        dados[chave] = pd.DataFrame(conteudo)

            except Exception as e:
                print(f"[ERRO] Ao carregar '{chave}': {e}")
        else:
            print(f"[AVISO] Arquivo não encontrado: {caminho}")

    return dados


# Carrega os dados corrigidos
dados = carregar_dados(arquivos)

# Verifica rapidamente o resultado
for nome, df in dados.items():
    print(f"→ {nome}: {df.shape[0]} linhas × {df.shape[1]} colunas")

#%% Verificação e definição de índice para os DataFrames com coluna 'id'
for nome, df in dados.items():
    print(f"\n🧾 {nome.upper()}")

    if 'id' in df.columns:
        # Mostra informações básicas
        print(f"✔ Coluna 'id' encontrada")
        print(f"→ Tipo de dado: {df['id'].dtype}")
        print(f"→ Exemplo de valores: {df['id'].dropna().unique()[:5]}")
        print(f"→ Valores únicos: {df['id'].nunique()}")
        print(f"→ Duplicados: {df.duplicated('id').sum()}")

        # Verifica se pode ser índice (sem duplicados ou nulos)
        if df['id'].isnull().any():
            print("Atenção: Existem valores nulos na coluna 'id'")
        elif df['id'].duplicated().any():
            print("Atenção: Existem IDs duplicados")
        else:
            # Define 'id' como índice
            df.set_index('id', inplace=True)
            dados[nome] = df
            print("Coluna 'id' definida como índice.")
    else:
        print("Coluna 'id' NÃO encontrada")
#%% Expansão e Normalização dos Dados
print(dados["prospeccoes"].columns)
print(dados["prospeccoes"].head())

#