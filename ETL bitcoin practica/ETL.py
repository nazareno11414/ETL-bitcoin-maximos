import pandas as pd
import plot
import bd_maximos as bd
#Cargar los datos
csv=pd.read_csv("Datos históricos del Bitcoin.csv")

#Convertir la fecha en formato fecha
csv['Fecha'] = pd.to_datetime(csv['Fecha'], format='%d.%m.%Y')

#Convertir los datos a float 
csv['Máximo'] = csv['Máximo'].str.replace('.', '', regex=False) 
csv['Máximo'] = csv['Máximo'].str.replace(',', '.', regex=False)
csv['Máximo'].astype(float)

#Guardar los datos en variables
x=csv['Fecha']
y=csv['Máximo']


bd.mostrar_datos()