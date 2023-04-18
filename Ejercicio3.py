import sqlite3
import pandas as pd
from matplotlib import pyplot as plt

con = sqlite3.connect('database.db')
cur = con.cursor()

dispositivos = pd.read_sql_query("SELECT * FROM dispositivos", con)
alertas = pd.read_sql_query("SELECT * FROM alertas", con)
analisis = pd.read_sql_query("SELECT * FROM analisis", con)

# Clasificamos por prioridad
## Hacemos join de las tablas de interes para correlacionar los datos
join_alertas_dispositivos = pd.read_sql_query("SELECT * FROM alertas JOIN dispositivos ON (alertas.origen = dispositivos.ip) JOIN analisis ON dispositivos.analisis = analisis.id", con)
for i in range(1, 4): # las prioridades posibles son 1, 2, 3
    if i == 1:
        print("### DATOS ALERTAS GRAVES ###")
    if i == 2:
        print("### DATOS ALERTAS MEDIAS ###")
    if i == 3:
        print("### DATOS ALERTAS BAJAS ###")
    prioridad = join_alertas_dispositivos.loc[join_alertas_dispositivos['prioridad'] == i]
    vulnerabilidades_detectadas = prioridad['vulnerabilidades_detectadas']
    print("Número de observaciones: " + str(len(prioridad)))
    print("Número de valores ausentes: " + str(len(prioridad.loc[prioridad['localizacion'] == 'None'])))
    print("Mediana: " + str(vulnerabilidades_detectadas.median()))
    print("Media: " + str(vulnerabilidades_detectadas.mean()))
    print("Varianza: " + str(vulnerabilidades_detectadas.var()))
    print("Valores máximo y mínimo: " + str(vulnerabilidades_detectadas.max()) + " y " + str(vulnerabilidades_detectadas.min()))
    print()

# Clasificamos por fecha
## Entendemos que hay que mostrar datos de Julio y Agosto
join_alertas_dispositivos['timestamp'] = pd.to_datetime(join_alertas_dispositivos['timestamp'], format='%Y-%m-%d %H:%M:%S')
alertas_julio = join_alertas_dispositivos.loc[(join_alertas_dispositivos['timestamp'].dt.month == 7)]
alertas_agosto = join_alertas_dispositivos.loc[(join_alertas_dispositivos['timestamp'].dt.month == 8)]
for i in range(0, 2):
    if i == 0:
        print("### DATOS ALERTAS JULIO ###")
        vulnerabilidades_detectadas = alertas_julio['vulnerabilidades_detectadas']
        print("Número de observaciones: " + str(len(alertas_julio)))
        print("Número de valores ausentes: " + str(len(alertas_julio.loc[alertas_julio['localizacion'] == 'None'])))
        print("Mediana: " + str(vulnerabilidades_detectadas.median()))
        print("Media: " + str(vulnerabilidades_detectadas.mean()))
        print("Varianza: " + str(vulnerabilidades_detectadas.var()))
        print("Valores máximo y mínimo: " + str(vulnerabilidades_detectadas.max()) + " y " + str(vulnerabilidades_detectadas.min()))
        print()
    if i == 1:
        print("### DATOS ALERTAS AGOSTO ###")
        vulnerabilidades_detectadas = alertas_agosto['vulnerabilidades_detectadas']
        print("Número de observaciones: " + str(len(alertas_agosto)))
        print("Número de valores ausentes: " + str(len(alertas_agosto.loc[alertas_agosto['localizacion'] == 'None'])))
        print("Mediana: " + str(vulnerabilidades_detectadas.median()))
        print("Media: " + str(vulnerabilidades_detectadas.mean()))
        print("Varianza: " + str(vulnerabilidades_detectadas.var()))
        print("Valores máximo y mínimo: " + str(vulnerabilidades_detectadas.max()) + " y " + str(vulnerabilidades_detectadas.min()))
        print()
