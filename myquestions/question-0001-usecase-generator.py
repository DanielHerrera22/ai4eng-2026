import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


import numpy as np
import pandas as pd

def generar_caso_de_uso_calcular_error_precio_casas():
    # Número aleatorio de muestras y características
    n_muestras = np.random.randint(50, 200)
    n_features = np.random.randint(2, 5)

    # Generar características
    X = np.random.rand(n_muestras, n_features) * 100

    # Generar variable objetivo (relación lineal + ruido)
    coeficientes = np.random.rand(n_features)
    ruido = np.random.randn(n_muestras) * 10
    y = X @ coeficientes + ruido

    # Convertir a pandas
    X_df = pd.DataFrame(X)
    y_series = pd.Series(y)

    # Solo retornar los datos
    return X_df, y_series

resultados= generar_caso_de_uso_calcular_error_precio_casas()
x= resultados[0]
y= resultados[1]
