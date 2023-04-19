import sqlite3
import pandas as pd
from matplotlib import pyplot as plt

con = sqlite3.connect('database.db')
cur = con.cursor()

### EJERCICIO 2 ###
dispositivos = pd.read_sql_query("SELECT * FROM dispositivos", con)
alertas = pd.read_sql_query("SELECT * FROM alertas", con)
analisis = pd.read_sql_query("SELECT * FROM analisis", con)

print("Número de dispositivos: " + str(len(dispositivos.index)))
print("Número de alertas: " + str(len(alertas.index)))

media_puertos_abiertos = analisis['n_puertos_abiertos'].mean()
desviacion_puertos_abiertos = analisis['n_puertos_abiertos'].std()
print("Media y desviación estándar del total de puertos abiertos: " + str(media_puertos_abiertos) + ", " +  str(desviacion_puertos_abiertos))

media_servicios_inseguros = analisis['servicios_inseguros'].mean()
desviacion_servicios_inseguros = analisis['servicios_inseguros'].std()
print("Media y desviación estándar del número de servicios inseguros detectados: " + str(media_servicios_inseguros) + ", " + str(desviacion_servicios_inseguros))

media_vulnerabilidades_detectadas = analisis['vulnerabilidades_detectadas'].mean()
desviacion_vulnerabilidades_detectadas = analisis['vulnerabilidades_detectadas'].std()
print("Media y desviación estándar del número de vulnerabilidades detectadas: " + str(media_vulnerabilidades_detectadas) + ", " + str(desviacion_vulnerabilidades_detectadas))

minimo_puertos = analisis['n_puertos_abiertos'].min()
maximo_puertos = analisis['n_puertos_abiertos'].max()
print("Valor mínimo y valor máximo del total de puertos abiertos: ", str(minimo_puertos) + ", " + str(maximo_puertos))

minimo_vulnerabilidades_detectadas = analisis['vulnerabilidades_detectadas'].min()
maximo_vulnerabilidades_detectadas = analisis['vulnerabilidades_detectadas'].max()
print("Valor mínimo y valor máximo del número de vulnerabilidades detectadas: ", str(minimo_vulnerabilidades_detectadas) + ", " + str(maximo_vulnerabilidades_detectadas))