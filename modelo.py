import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#nuestros dataframes que usaremos debe ser un csv y contener bien  datos como fechas  nombre de la accion
datos =''
df= pd.read_csv(datos)
df.set_index('Date', inplace =True)
df

#variables
a1 = 'nombre de la accion 1'
a2  = 'nombre de la accion 2'
x = df[a1]
y = df[a2]

##nos mostrara como esta la dispersion de los datos que tengaamos
plt.figure(figsize=(8,6))
plt.scatter(x,y, alpha=0.3)

plt.title(f"precio de {a1} vs {a2}")
plt.xlabel(a1)
plt.ylabel(a2)

plt.grid(True, linestile ="--", alpha =0.4)
plt.tight_layout()
plt.show

## empezamos con regresion lineal
X = df[a1].values
Y = df[a2].values
n= len(X) #el tamaño de X y Y deben ser iguales

mX = np.mean(X)
mY= np.mean(Y)

#calculando sus sumas  de dato real menos la media.
Sxx = np.sum((X - mean_X) ** 2)
Sxy = np.sum((X - mean_X) * (Y - mean_Y))

# Calcular los coeficientes de la recta de regresión
b1 = Sxy / Sxx
b0 = mean_Y - b1 * mean_X
# Ecuacion de la recta de regresion
print(f'La ecuacion de la recta de regresion es: Y_est = {b0:.2f} + {b1:.2f} *␣
↪X ')
y_est = b0 + b1 * X # Y_est = b0 + b1 * X

#grafico con la recta correspondiente
plt.figure(figsize=(9,6))
plt.scatter(df['^SPX'], df['AAPL'], alpha=0.6, label="Datos reales")
# Recta de regresión
plt.plot(X, y_est, linewidth=2.5, label="Recta de regresión", color="red")

plt.title("Precio de AAPL vs SPX")
plt.xlabel("SPX (^SPX)")
plt.ylabel("AAPL")
plt.grid(True, linestyle="--", alpha=0.4)
plt.legend()
plt.tight_layout()
plt.show()
