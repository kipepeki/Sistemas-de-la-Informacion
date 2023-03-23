import sqlite3
import pandas as pd


con = sqlite3.connect('database.db')
cur = con.cursor()

## Creamos las tablas DISPOSITIVOS, RESPONSABLES y ANALISIS
cur.execute('''CREATE TABLE IF NOT EXISTS dispositivos (
                        id TEXT,
                        ip TEXT PRIMARY KEY,
                        localizacion TEXT,
                        responsable TEXT,
                        analisis INTEGER
)''')
cur.execute('''CREATE TABLE IF NOT EXISTS responsables (
                        nombre TEXT PRIMARY KEY,
                        telefono TEXT,
                        rol TEXT
)''')
cur.execute('''CREATE TABLE IF NOT EXISTS analisis (
                        puertos_abiertos TEXT,
                        n_puertos_abiertos INTEGER,
                        servicios INTEGER,
                        servicios_inseguros INTEGER,
                        vulnerabilidades_detectadas INTEGER
)''')

## Creamos tabla ALERTAS con el propio pandas ya que el formato de los datos permiten crearla directamente (primera fila del .csv)
alerts = pd.read_csv("./data/alerts.csv")
alerts.to_sql("alertas", con, if_exists="replace", index=False)

con.commit()
con.close()

