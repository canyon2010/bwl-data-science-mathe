import pandas as pd

# 1. Die bekannten Daten laden
data = {
    "Kunden_ID": [f"K-{i}" for i in range(1001, 1011)],
    "Monatliche_Kosten": [29.99, 49.95, 19.99, 79.90, 34.99, 59.95, 89.99, 24.50, 39.99, 69.95],
    "Gekuendigt_Reallitaet": [0, 1, 0, 0, 1, 0, 0, 1, 0, 0]  # 1=Ja, 0=Nein
}
df = pd.DataFrame(data)

# 2. DEINE REGEL ANWENDEN: Wenn Kosten < 30 Euro, dann Vorhersage = 1 (Kündigung)
# Das 'astype(int)' macht aus True/False wieder 1/0
df["Vorhersage_Modell"] = (df["Monatliche_Kosten"] < 30.00).astype(int)

# 3. PRÜFUNG: Wo lag das Modell richtig?
df["Richtig_Prognostiziert"] = df["Gekuendigt_Reallitaet"] == df["Vorhersage_Modell"]

# Tabelle für den Vertriebsleiter ausgeben
print(df[["Kunden_ID", "Monatliche_Kosten", "Gekuendigt_Reallitaet", "Vorhersage_Modell", "Richtig_Prognostiziert"]])

# Treffsicherheit (Accuracy) berechnen
treffsicherheit = df["Richtig_Prognostiziert"].mean() * 100
print(f"\nGesamte Treffsicherheit deines Modells: {treffsicherheit}%")
