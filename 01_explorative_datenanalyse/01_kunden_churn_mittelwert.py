import pandas as pd

# 1. Daten in eine professionelle Tabelle (DataFrame) packen
data = {
    "Monatliche_Kosten": [29.99, 49.95, 19.99, 79.90, 34.99, 59.95, 89.99, 24.50, 39.99, 69.95],
    "Gekuendigt": ["Nein", "Ja", "Nein", "Nein", "Ja", "Nein", "Nein", "Ja", "Nein", "Nein"]
}
df = pd.DataFrame(data)

# 2. DEIN ANSATZ: Nach Kündigungsstatus gruppieren und den Mittelwert berechnen
mittelwerte = df.groupby("Gekuendigt")["Monatliche_Kosten"].mean()

# 3. Ergebnis anzeigen
print(mittelwerte.round(2))
