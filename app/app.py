import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title="Decision AI Recruiter", layout="centered")

st.title("🤖 IA para Recrutamento - Decision")
st.markdown("Preencha os dados do candidato para obter a previsão de compatibilidade com a vaga.")

# Exemplo de campos simulados
nome = st.text_input("Nome do candidato")
experiencia = st.slider("Anos de experiência", 0, 20, 2)
linguagem = st.selectbox("Linguagem principal", ["Python", "Java", "JavaScript", "Outros"])
motivacao = st.slider("Grau de motivação percebida (0-10)", 0, 10, 5)

if st.button("Analisar Match"):
    try:
        model = joblib.load("models/best_model.pkl")
        input_df = pd.DataFrame([{
            "experiencia": experiencia,
            "linguagem": linguagem,
            "motivacao": motivacao
        }])
        # Pré-processamento fictício (deve ser igual ao usado no treino)
        input_df['linguagem'] = input_df['linguagem'].map({
            "Python": 0, "Java": 1, "JavaScript": 2, "Outros": 3
        })
        resultado = model.predict_proba(input_df)[0][1]
        st.success(f"Probabilidade de match: {resultado:.2%}")
    except Exception as e:
        st.error(f"Erro ao carregar o modelo ou processar dados: {e}")
