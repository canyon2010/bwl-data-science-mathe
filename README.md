Wirtschaftsmathematische KI-Kundenabwanderungsvorhersage (Telco Churn Prediction)
Dieses Repository enthält ein End-to-End-Projekt im Bereich Data Science & Predictive Analytics, das die mathematischen Grundlagen einer binären Klassifikation mit strategischen Business-Coaching-Ansätzen zur Risikominimierung in Unternehmen verknüpft.
---
🚀 Kern-Ergebnisse & Business-Impact
Strategische Schwellenwert-Optimierung (Threshold Shift):
Durch das Absenken des Klassifikations-Schwellenwerts von `0.5` auf `0.3` wurde das Fangnetz für wechselwillige Kunden drastisch vergrößert.
Maximierung des Recalls auf 78 %: Das Modell identifiziert nun rechtzeitig 78 % aller tatsächlichen Abwanderer (Klasse 1), wodurch das finanzielle Verlustrisiko des Unternehmens minimiert wird.
Identifikation des stärksten Churn-Treibers: Die mathematische Analyse isolierte Glasfaser-Internet (Beta-Gewicht: +1.077) als primäre Kündigungsfalle, was als direkte Steilvorlage für strategische Produkt- und Service-Workshops im Management dient.
---
📊 Mathematisches Fundament (Logistische Regression)
Da die Zielvariable binär ist ($y \in {0, 1}$), quetscht die klassische lineare Regression Vorhersagen fälschlicherweise über diesen Bereich hinaus. Dieses Modell nutzt die Logit-Transformation, um die Skala der Wahrscheinlichkeit $p$ künstlich auf den unendlichen Bereich von $-\infty$ bis $+\infty$ aufzublasen, damit sie mit der Regressionsgeraden gleichgesetzt werden kann:
$$\ln\left(\frac{p}{1-p}\right) = \beta_0 + \beta_1 \cdot x_1 + \beta_2 \cdot x_2 + \dots + \beta_n \cdot x_n = z$$
Durch die Auflösung nach der gesuchten Wahrscheinlichkeit $p$ entsteht die Sigmoid-Funktion:
$$p = \frac{1}{1 + e^{-z}}$$
Optimierung (Gradient Descent & Log-Loss)
Die Gewichte ($\beta$) werden iterativ über den Gradientenabstieg bestimmt. Als Kostenfunktion dient der konvexe Log-Loss (Binary Cross-Entropy), welcher falsche Vorhersagen durch den natürlichen Logarithmus exponentiell hart bestraft:
$$\text{Loss} = -\Big( y \cdot \ln(p) + (1-y) \cdot \ln(1-p) \Big)$$
---
🛠️ Projektschritte im Jupyter Notebook
Exploratory Data Analysis (EDA) & Deskriptive Statistik: Untersuchung von Häufigkeitsverteilungen und stochastischen Ungleichgewichten (Imbalanced Data: 26,5 % Churn-Quote).
Data Cleaning & Preprocessing: Identifikation und Bereinigung von Formatierungsfehlern (Konvertierung von `TotalCharges` von `object` zu `float64` und Handling von Missing Values).
Feature Engineering: Transformation kategorischer Variablen mittels One-Hot-Encoding unter Vermeidung von Multikollinearität (`drop_first=True`).
Modell-Training & Evaluierung: Aufteilung der Daten (80/20 Train-Test-Split) mit fixiertem `random_state=42` für reproduzierbare Ergebnisse. Evaluierung mittels Confusion Matrix, Precision und Recall.
---
🧠 Business-Coaching-Perspektive: Warum Glasfaser der Treiber ist
Ein hoher positiver Beta-Wert von +1.077 bei Glasfaser-Kunden zeigt ein typisches Erwartungs-Dilemma in Großkonzernen:
Das Service-Defizit: Teure Highspeed-Produkte erzeugen hohe Kundenerwartungen. Versagen der Kundenservice oder die Hardware (WLAN-Abdeckung im Haus), kippt die Zufriedenheit sofort in Frustration.
Der Preisschock: In Kombination mit den Gesamtgebühren (`TotalCharges`) reagieren Kunden hochsensibel auf monatliche Fixkosten und wechseln aktiv zu günstigeren DSL-Anbietern.
Strategische Lösung: Als Business Coach wird dem Management empfohlen, den Fokus von der reinen Neukundenakquise auf proaktive Service-Anrufe und technische Set-up-Hilfen für bestehende Glasfaser-Kunden zu lenken.
---
📦 Technische Voraussetzungen (Stack)
Sprache: Python 3.x
Umgebung: Anaconda / Jupyter Notebook
Bibliotheken: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`
---
📝 Lizenz
Dieses Projekt ist für Portfolio- und Bewerbungszwecke frei zugänglich. Created by a Business Coach & Wirtschaftsmathematiker.
