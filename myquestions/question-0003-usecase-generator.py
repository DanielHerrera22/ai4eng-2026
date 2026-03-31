import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def generar_datos_sensores(n_muestras=500, n_variables=50):
    # Generar datos aleatorios (simulando sensores)
    datos = np.random.randn(n_muestras, n_variables) * 10 + 50

    # Escalar (muy importante para PCA)
    scaler = StandardScaler()
    datos_escalados = scaler.fit_transform(datos)

    return datos_escalados  # numpy.ndarray

datos = generar_datos_sensores()

X_reducido, n_componentes = reducir_dimensiones_pca(datos, 0.95)
