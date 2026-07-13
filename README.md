# bwl-data-science-mathe
Mathematische Grundlagen, KPIs und Machine Learning angewendet auf betriebswirtschaftliche Datensätze für Geschäftsentscheidungen

# Business Analytics & Machine Learning Portfolio

Dieses Repository schlägt die Brücke zwischen höherer Mathematik, Datenanalyse mit Python und echten, datengetriebenen Geschäftsentscheidungen für die Unternehmensführung.

---

## Projekt 1: Kunden-Abwanderungsanalyse (Churn Prediction)

### 📈 Das Business-Szenario (Anforderungsanalyse)
Der Vertriebsleiter meldet eine kritische Wechselquote bei den Vertragskunden. Es liegt ein historischer Datensatz von Kunden vor (Monatliche Kosten in € und Kündigungsstatus). Die Aufgabe bestand darin, den mathematischen Zusammenhang zu analysieren, ein Vorhersagemodell zu entwickeln und eine konkrete Handlungsempfehlung für die Geschäftsführung abzuleiten.

### 🛠 Methodisches Vorgehen & Projektstruktur

Der komplette Data-Science-Zyklus wurde in drei iterative Schritte unterteilt (zu finden im Ordner `02_bwl_case_studies/`):

1. **`01_kunden_churn_mittelwert.py` | Explorative Datenanalyse (EDA)**
   * **Ansatz:** Gruppierung der Daten nach dem Kündigungsstatus mittels `pandas.groupby()`.
   * **Ergebnis:** Widerlegung der Hypothese, dass Kunden aufgrund zu hoher Preise kündigen. Treue Kunden zahlen im Schnitt ~49,68 €, während Kündiger im Schnitt nur ~36,48 € zahlen. Das Problem liegt im Niedrigpreissegment.

2. **`02_kunden_churn_prognose.py` | Regelbasiertes Basis-Modell (Baseline)**
   * **Ansatz:** Formulierung einer intuitiven Business-Regel als Schwellenwert (Kosten < 30 € $\rightarrow$ Kündigung).
   * **Ergebnis:** Dieses simple, transparente Modell erzielt ohne algorithmischen Rechenaufwand sofort eine Treffsicherheit (Accuracy) von **70,0 %**.

3. **`03_kunden_churn_ki_modell.py` | Machine Learning Optimierung**
   * **Ansatz:** Training eines Entscheidungsbaums (`scikit-learn.tree.DecisionTreeClassifier`) mit begrenzter Tiefe (`max_depth=1`). Der Algorithmus sucht vollautomatisch nach dem mathematisch optimalen Schwellenwert (Gini-Split).
   * **Ergebnis:** Das ML-Modell optimiert den Schwellenwert auf **54,95 €**. Es fängt damit erfolgreich 100 % aller Kündiger ein (hoher Recall), erreicht aufgrund der kleinen Datenbasis in der Gesamt-Treffsicherheit aber ebenfalls **70,0 %**.

### 💼 Entscheidungsvorlage für die Geschäftsführung (ROI & Impact)
* **Erkenntnis:** Kunden wandern uns nicht ab, weil wir zu teuer sind, sondern weil im Billigsegment unterhalb von ~55 € die Kundenbindung fehlt.
* **Handlungsempfehlung:** Da das Machine-Learning-Modell bei 54,95 € alle potenziellen Kündiger identifiziert, sollte die Marketingabteilung automatisiert für alle Kunden mit Tarifen unter 55 € ein gezieltes Service- oder Upgrade-Angebot auslösen, um die Abwanderung frühzeitig zu blockieren. Ein teurerer Ausbau der KI-Infrastruktur ist bei der aktuellen Datenlage wirtschaftlich nicht sinnvoll, da die einfache Business-Logik bereits dieselbe Genauigkeit liefert.

