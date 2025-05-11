import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

from preprocessing import preprocess_data

# Carregar dados
df = pd.read_csv("data/processed/base_tratada.csv")
df = preprocess_data(df)

X = df.drop("match", axis=1)
y = df["match"]

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

# Treinar modelo
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Avaliar modelo
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Salvar modelo
joblib.dump(model, "models/best_model.pkl")
