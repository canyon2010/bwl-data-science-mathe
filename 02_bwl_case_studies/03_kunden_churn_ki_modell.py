import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# 1. Die bekannten Daten laden
data = {
    "Monatliche_Kosten": [29.99, 49.95, 19.99, 79.90, 34.99, 59.95, 89.99, 24.50, 39.99, 69.95],
    "Gekuendigt": [0, 1, 0, 0, 1, 0, 0, 1, 0, 0]  # 1=Ja, 0=Nein
}
df = pd.DataFrame(data)

# 2. Daten für die KI vorbereiten
# X sind die Merkmale (muss zweidimensional sein), y ist das Ziel
X = df[["Monatliche_Kosten"]]
y = df["Gekuendigt"]

# 3. DAS KI-MODELL: Entscheidungsbaum initialisieren und mit Daten trainieren
# Wir begrenzen die Tiefe (max_depth) auf 1, damit er exakt nur EINE Trennlinie sucht
modell = DecisionTreeClassifier(max_depth=1, random_state=42)
modell.fit(X, y)

# 4. Der mathematische Clou: Welchen Schwellenwert hat die KI gefunden?
schwellenwert = modell.tree_.threshold[0]
print(f"Die KI hat den optimalen Schwellenwert berechnet bei: {schwellenwert:.2f} Euro\n")

# 5. Vorhersage für die 10 Kunden treffen und Treffsicherheit berechnen
df["KI_Vorhersage"] = modell.predict(X)
treffsicherheit = (df["Gekuendigt"] == df["KI_Vorhersage"]).mean() * 100
print(f"Gesamte Treffsicherheit des KI-Modells: {treffsicherheit}%")
