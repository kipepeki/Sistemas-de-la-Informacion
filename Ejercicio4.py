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

dispositivos = pd.read_sql_query("SELECT * FROM dispositivos", con)
alertas = pd.read_sql_query("SELECT * FROM alertas", con)
analisis = pd.read_sql_query("SELECT * FROM analisis", con)
merge = pd.merge(dispositivos, analisis, on='ip')

merge = pd.merge(dispositivos, analisis, on='ip')
vuln = analisis[['servicios_inseguros', 'vulnerabilidades_detectadas']]
vuln['suma_vuln'] = vuln['servicios_inseguros'] + vuln['vulnerabilidades_detectadas']
vuln_dispositivo = pd.concat([merge['ip'], vuln['suma_vuln']], axis=1)
vuln_dispositivo_agrupado = vuln_dispositivo.groupby('ip').sum().reset_index()
vuln_dispositivo_ordenado = vuln_dispositivo_agrupado.sort_values(by='suma_vuln', ascending=False)
top_10 = vuln_dispositivo_ordenado.head(10)
top_10 = top_10[['ip', 'suma_vuln']]
plt.bar(top_10['ip'], top_10['suma_vuln'])
plt.xlabel('IP dispositivo')
plt.ylabel('Vulnerabilidades')
plt.title('Top 10 Dispositivos vulnerables')
plt.show()

n_alertas = alertas.groupby('clasificacion').size().reset_index(name='count')
plt.bar(n_alertas['clasificacion'], n_alertas['count'])
plt.xlabel('Categoría')
plt.ylabel('Numero de alertas')
plt.title('Alertas por categoría')
plt.xticks(rotation=90)
plt.show()

media_p_abiertos = merge['n_puertos_abiertos'].mean()
media_p_abiertos_s_inseguros = merge['n_puertos_abiertos'].mean() / merge['servicios_inseguros'].mean()
media_p_abiertos_s_detectados = merge['n_puertos_abiertos'].mean() / merge['servicios'].mean()
medias_p_servicios = pd.Series([media_p_abiertos_s_inseguros, media_p_abiertos_s_detectados])
medias_p_servicios.index = ['P abiertos vs S inseguros', 'P abiertos vs S detectados']
medias_p_servicios.plot(kind='barh')
plt.xlabel('Media')
plt.title('Comparación de medias')
plt.show()

print('Media de puertos abiertos frente a servicios inseguros:', media_p_abiertos_s_inseguros)
print('Media de puertos abiertos frente al total de servicios detectados:', media_p_abiertos_s_detectados)