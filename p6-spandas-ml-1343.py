import pandas as pd
import numpy as np

series_amigos=["pedro","Morgan","Farfan","El Adrian","Jesse","Eliseo","Mario"]
print("--- serie listado de amigos NC=1343 ---")
amigos=pd.Series(series_amigos)
print(amigos)

series_billetes=[20,50,100,200,500,1000]
print("--- serie listado de valor de billetes MX NC=1343 ---")
amigos=pd.Series(series_billetes)
print(amigos)

series_billetes=[20,50,100,200,500,1000]
serie_bletras=["veinte","cincuentea","cien","docientos","quinientos","mil"]
print("--- serie listado de valor de billetes MX NC=1343 ---")
tablabilletes=pd.Series(serie_bletras, series_billetes)
print(tablabilletes)
# diccionario dataframe
# diccionario de valor monedas y nombre
print("datos de diccionario a dataframe en pandas")
dic_monedas ={
    "serie_billetes":[20,50,100,200,500,1000],
    "serie_bletras":["veinte","cincuenta","cien","docientos","quinientos","mil"]

}

tablabilletes=pd.DataFrame(dic_monedas, index=["A","B","C","D","E","F"])
print(tablabilletes)
print("Casa de cambio de Daniel Nieves NC=1343")