import numpy as np
import pandas as pd

def generar_datos_fraude(n_muestras=1000, n_features=10, ratio_fraude=0.05):
    # Variables numéricas (simulando transacciones)
    X = np.random.randn(n_muestras, n_features)

    # Etiquetas desbalanceadas (pocos fraudes)
    y = np.zeros(n_muestras)
    n_fraudes = int(n_muestras * ratio_fraude)

    indices_fraude = np.random.choice(n_muestras, n_fraudes, replace=False)
    y[indices_fraude] = 1

    return X, y

X, y = generar_datos_fraude()

score = evaluar_modelo_fraude_cv(X, y, 5)
