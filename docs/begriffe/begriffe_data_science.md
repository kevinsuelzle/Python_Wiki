# Begriffssammlung Data Science


# Einführung in Data Science

| Begriff        | Kurzerklärung                                               | Link zur Referenz                                      |
|----------------|-------------------------------------------------------------|--------------------------------------------------------|
| Data Science   | Eine Fachdisziplin, um aus Daten neues Wissen zu generieren | [Referenz](https://de.wikipedia.org/wiki/Data_Science) |

# Pandas: Einführung

| Begriff                   | Kurzerklärung                                                         | Link zur Referenz                                                                   |
|---------------------------|-----------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| `DataFrame`               | Datenstruktur in Pandas, die eine Tabelle speichert                   | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)      |
| `Series`                  | Datenstruktur in Pandas, die eine Folge von Werten speichert          | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.Series.html)         |
| `Index`                   | Die Beschriftung der Zeilen einer Pandas Tabelle                      | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.Index.html)          |
| `.loc[]`                  | Zugriff auf eine Zeile in einer Pandas Tabelle über Zeilenbezeichnung | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html)  |
| `concat()`                | Zusammenfügen mehreren DataFrames oder Series'                        | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.concat.html)         |
| 

# Pandas: Import/Export von Daten

| Begriff                   | Kurzerklärung                                                         | Link zur Referenz                                                                        |
|---------------------------|-----------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| `read_csv()`              | Liest eine `.csv` (comma separated values) Datei ein (eine Tabelle)   | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)            |
| `to_csv()`                | Speichert eine Pandas Tabelle als `.csv`-Datei                        | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html)    |
| `to_dict()`               | Wandelt eine Tabelle in ein Python Dictionary um                      | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html)   |
| `read_pickle()`           | Liest eine Pandas Tabelle aus einer pickle-Datei                      | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.read_pickle.html)         |
| `to_pickle()`             | Speichert eine Pandas Tabelle im pickle-Dateiformat (Binärdatei)      | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_pickle.html) |
| `to_sql()`                | Speichert eine Pandas Tabelle in einer SQL-Datenbank                  | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html)    |
| `read_sql_query()`        | Führt einen SQL-Befehl aus einer SQL-Datenbank aus. Ergebnis: Tabelle | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.read_sql_query.html)      |


# Pandas: Fehlende Werte

| Begriff                   | Kurzerklärung                                                                | Link zur Referenz                                                                          |
|---------------------------|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| `NaN`                     | Steht für "Not a Number". Im Kontext von Tabellen meint dies eine Datenlücke | [Referenz](https://de.wikipedia.org/wiki/NaN)                                              |
| Imputation                | Einfügen von Werten in Datenlücken                                           | [Referenz](https://de.wikipedia.org/wiki/Imputation_(Statistik))                           |
| `isnull()`                | Hilfsfunktion, um fehlende Werte in Pandas DataFrames/Series zu detektieren  | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.isnull.html)                |
| `dropna()`                | Entfernt unvollständige Zeilen oder Spalten in einer Tabelle bzw. Series     | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html)      |
| `fillna()`                | Füllt Datenlücken (`NaN`) mit Werten                                         | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html)      |
| `median()`                | Berechnet den Median über Zeilen oder Spalten (je nach Einstellung)          | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.median.html)      |
| `interpolate()`           | Füllt Datenlücken mit Hilfe von benachbarten Werten (Randwerten)             | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.interpolate.html) |


# NumPy: Einführung und NumPy Arrays

| Begriff                   | Kurzerklärung                                                          | Link zur Referenz                                                                             |
|---------------------------|------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| `numpy.array()`           | Ein n-dimensionales Array. Wird sehr effizient gespeichert             | [Referenz](https://numpy.org/doc/stable/reference/generated/numpy.array.html)                 |
| `arange()`                | Erzeugt ein NumPy Array in einem angegebenen Bereich                   | [Referenz](https://numpy.org/doc/stable/reference/generated/numpy.arange.html)                |
| `sum()`                   | Bildet die Zeilen- oder Spaltensummen eines Arrays                     | [Referenz](https://numpy.org/doc/stable/reference/generated/numpy.sum.html)                   |
| `max()`                   | Berechnet das Zeilen- oder Spaltenmaximum eines Arrays                 | [Referenz](https://numpy.org/doc/stable/reference/generated/numpy.max.html)                   |
| `multiply()`              | Multipliziert zwei Arrays elementweise (keine Matrizenmultiplikation!) | [Referenz](https://numpy.org/doc/stable/reference/generated/numpy.multiply.html)              |
| `randint()`               | Erzeugt ein Array mit zufälligen ganzen Zahlen aus einem Intervall     | [Referenz](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html) |
| `transpose()`             | Wandelt Zeilen einer Matrix in Spalten um ("kippt" die Matrix)         | [Referenz](https://numpy.org/doc/stable/reference/generated/numpy.transpose.html)             |


# Numpy: Slicing

| Begriff                   | Kurzerklärung                                                                   | Link zur Referenz                                                                                      |
|---------------------------|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| Slicing                   | Bei Python-Listen, NumPy-Arrays oder Tabellen Teile "herrauschneiden"           | [Referenz](https://www.geeksforgeeks.org/slicing-indexing-manipulating-and-cleaning-pandas-dataframe/) |
| Boolean Indexing          | Rausschneiden von Teilen eines NumPy-Arrays, das gewissen Bedingungen "genügt"  | [Referenz](https://numpy.org/doc/stable/user/basics.indexing.html)                                     |
| `diagonal()`              | Liefert die Diagonalwerte einer Matrix                                          | [Referenz](https://numpy.org/doc/stable/reference/generated/numpy.diagonal.html)                       |
| `reshape()`               | Wandelt die Werte eines NumPy-Arrays in einer andere Form (Dimensionalität) um  | [Referenz](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html)                        |


# Matplotlib: Linienplots

| Begriff                   | Kurzerklärung                                                                     | Link zur Referenz                                                                                      |
|---------------------------|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| `plot()`                  | Plottet (x,y)-Punkte mit Markern und/oder verbindet diese mit Linien (Linienplot) | [Referenz](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)                      |
| Marker                    | Visualisiert einzelne Datenpunkte über Kreise, Dreiecke, Sterne, etc.             | [Referenz](https://matplotlib.org/stable/api/markers_api.html)                                         |
| `annotate()`              | Erlaubt es Anmerkungen zu einzelnen Datenpunkte über Pfeile+Text hinzuzufügen     | [Referenz](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.annotate.html)                  |
| `plt.legend()`            | Fügt einem Diagramm eine Legende zu, die zeigt, was die einzelnen Linien bedeuten | [Referenz](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html)                    |
| `plt.grid()`              | Zeigt Gitterlinien im Diagramm an. Erhöht die Lesbarkeit                          | [Referenz](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html)                      |


# Matplotlib: Subplots

| Begriff                   | Kurzerklärung                                                                   | Link zur Referenz                                                                                      |
|---------------------------|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| Subplot                   | Ein Unterdiagramm in einem großen Diagramm                                      | [Referenz](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html)         |
| `plt.subplot()`           | Fügt einen neuen einzelnen Subplot (Unterdiagramm) hinzu                        | [Referenz](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html)                   |
| `plt.subplots()`          | Erzeugt eine ganze Menge (ein Gitter) von Subplots                              | [Referenz](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html)                  |
| `tight_layout()`          | Optimiert die Abstände zwischen und um Subplots herum                           | [Referenz](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html)              |
| `subplots_adjust()`       | Erlaubt es horizontale und vertikale Abstände zwischen Subplots zu definieren   | [Referenz](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html)           |
| `subplot2grid()`          | Erlaubt es Subplots über mehrere Zeilen/Spalten des Subplotgitters zu erzeugen  | [Referenz](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot2grid.html)              |


# Seaborn: Einführung


| Begriff                   | Kurzerklärung                                                                   | Link zur Referenz                                                                                      |
|---------------------------|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| `violinplot()`            | Plot, der die Verteilung von Daten und einen Boxplot gleichzeitig visualisiert  | [Referenz](https://seaborn.pydata.org/generated/seaborn.violinplot.html)                               |
| `countplot()`             | Balkendiagramm, das zeigt, wie oft bestimmte Kategorien auftreten               | [Referenz](https://seaborn.pydata.org/generated/seaborn.countplot.html)                                |
| `boxplot()`               | Visualiert Median, Quartile, Spannweiter und Ausreißer in einem Diagramm        | [Referenz](https://seaborn.pydata.org/generated/seaborn.boxplot.html)                                  |
| FacetGrid                 | Plot, der es erlaubt schnell bedingte Abhängigkeiten zwischen Daten zu erkennen | [Referenz](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html)                                |
| `jointplot()`             | Kombination von Scatterplot und Histogramm-Plots                                | [Referenz](https://seaborn.pydata.org/generated/seaborn.jointplot.html)                                |
| `kdeplot()`               | Zeigt Verteilungen von Daten über Isokonturlinien ("Höhenlinien") an            | [Referenz](https://seaborn.pydata.org/generated/seaborn.kdeplot.html)                                  |


# Matplotlib: Ticks

| Begriff                             | Kurzerklärung                                                                                             | Link zur Referenz                                                                           |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| Ticks (bei Matplotlib Diagrammen)   | Ticks sind die Markierungen auf den Achsen eines Matplotlib-Diagramms, die die Skalenwerte repräsentieren | [Referenz](https://matplotlib.org/stable/users/explain/axes/axes_ticks.html)                |
| `xticks()`                          | Definiert, wo die Ticks auf der x-Achse gesetzt werden                                                    | [Referenz](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html)         |
| `yticks()`                          | Definiert, wo die Ticks auf der y-Achse gesetzt werden                                                    | [Referenz](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html)         |
| `xscale()`                          | Setzt die Skala (linear, logarithmisch) für die x-Achse                                                   | [Referenz](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xscale.html)         |
| `yscale()`                          | Setzt die Skala (linear, logarithmisch) für die y-Achse                                                   | [Referenz](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yscale.html)         |
| `tick_params()`                     | Erlaubt es z.B. die Farbe der Ticks zu ändern                                                             | [Referenz](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html) |


# Pandas: Multiindex

| Begriff                   | Kurzerklärung                                                                   | Link zur Referenz                                                                                      |
|---------------------------|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
|                    |            | [Referenz]() |
|                    |            | [Referenz]() |
|                    |            | [Referenz]() |
|                    |            | [Referenz]() |
|                    |            | [Referenz]() |
|                    |            | [Referenz]() |
|                    |            | [Referenz]() |

# Pandas: Gruppieren und Pivotisieren

| Begriff                   | Kurzerklärung                                                                   | Link zur Referenz                                                                                      |
|---------------------------|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
|                    |            | [Referenz]() |
|                    |            | [Referenz]() |
|                    |            | [Referenz]() |
|                    |            | [Referenz]() |
|                    |            | [Referenz]() |
|                    |            | [Referenz]() |
|                    |            | [Referenz]() |

# Pandas & Matplotlib: Zeitreihenanalyse

| Begriff                   | Kurzerklärung                                                                   | Link zur Referenz                                                                                      |
|---------------------------|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
|                    |            | [Referenz]() |
|                    |            | [Referenz]() |
|                    |            | [Referenz]() |
|                    |            | [Referenz]() |
|                    |            | [Referenz]() |
|                    |            | [Referenz]() |
|                    |            | [Referenz]() |

# Pandas: Outlier (Ausreißer)

| Begriff                   | Kurzerklärung                                                                   | Link zur Referenz                                                                                      |
|---------------------------|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
|                    |            | [Referenz]() |
|                    |            | [Referenz]() |
|                    |            | [Referenz]() |
|                    |            | [Referenz]() |
|                    |            | [Referenz]() |
|                    |            | [Referenz]() |
|                    |            | [Referenz]() |

# Pandas & Matplotlib: DateTime (Zeitstempel)

| Begriff                   | Kurzerklärung                                                                   | Link zur Referenz                                                                                      |
|---------------------------|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
|                    |            | [Referenz]() |
|                    |            | [Referenz]() |
|                    |            | [Referenz]() |
|                    |            | [Referenz]() |
|                    |            | [Referenz]() |
|                    |            | [Referenz]() |
|                    |            | [Referenz]() |





| Fachbegriff                          | Erläuterung                                                                                                                          |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------|



| Multiindex | Ein Multiindex in Pandas ermöglicht es, mehrere Indexebenen in einem DataFrame oder einer Series zu haben, wodurch komplexere Datenstrukturen dargestellt werden können |
| Gruppen (bei Pandas) | Gruppen in Pandas beziehen sich auf das Ergebnis der groupby-Operation, die Daten anhand gemeinsamer Merkmale in Untergruppen segmentiert, um Aggregations-, Transformations- oder Filteroperationen durchzuführen |
| Pivottabellen | Eine Pivottabelle in Pandas ist eine Datenzusammenfassungstabelle, die häufig für die interaktive Analyse und das Umstrukturieren von Daten, insbesondere zur Segmentierung und Aggregation, verwendet wird |
| Zeitreihe | Eine zeitlich geoordnete Folge von Werten, z.B. Sensorwerte einer Maschine oder Umsatzzahlen eines Unternehmens |
| IQR                 | Der Interquartilbereich (IQR) ist die Differenz zwischen dem 75. und 25. Perzentil eines Datensatzes und wird verwendet, um Ausreißer zu identifizieren. |
| Z-Score             | Der Z-Score ist eine statistische Maßzahl, die angibt, wie viele Standardabweichungen ein Datenpunkt vom Mittelwert der Datenmenge entfernt ist. |
| Winsorizing         | Winsorizing ist eine Methode zur Reduzierung von Ausreißern, indem extrem hohe und niedrige Werte auf einen bestimmten Perzentilwert gesetzt werden. |
| Quantil             | Ein Quantil ist ein Wert, der einen Datensatz in gleich große, aufeinanderfolgende Teile teilt, wobei das 50. Perzentil beispielsweise dem Median entspricht. |
| Standardabweichung  | Die Standardabweichung ist ein Maß für die Streuung der Werte in einem Datensatz, wobei höhere Werte auf eine größere Variabilität hinweisen. |
