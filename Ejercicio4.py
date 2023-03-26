import sqlite3
import pandas as pd
from matplotlib import pyplot as plt


con = sqlite3.connect('database.db')
cur = con.cursor()
alertas = pd.read_sql_query("SELECT * FROM alertas", con)
top_10_ips = alertas[alertas['prioridad'] == 1].groupby('origen').size().nlargest(10).reset_index(name='count')
plt.bar(top_10_ips['origen'], top_10_ips['count'])
plt.xlabel('IP')
plt.ylabel('Alertas prioridad 1')
plt.show()

alertas['timestamp'] = pd.to_datetime(alertas['timestamp'])
# Agrupamos por timestamp y contamos el número de columnas en ese timestamp
n_alertas = alertas.groupby('timestamp').size().reset_index(name='count')
plt.plot(n_alertas['timestamp'], n_alertas['count'])
plt.xlabel('Timestamp')
plt.ylabel('Numero alertas')
plt.title('Alertas en el tiempo')
plt.show()