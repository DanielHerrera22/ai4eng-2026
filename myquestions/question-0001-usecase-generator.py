import numpy as np
import pandas as pd

def generar_caso_de_uso_calcular_error_precio_casas():
    n_muestras = np.random.randint(50, 200)
    n_features = np.random.randint(2, 5)

    X = np.random.rand(n_muestras, n_features) * 100

    coeficientes = np.random.rand(n_features)
    ruido = np.random.randn(n_muestras) * 10
    y = X @ coeficientes + ruido

    X_df = pd.DataFrame(X)
    y_series = pd.Series(y)

    info = {
        "descripcion": "Cálculo de error en predicción de precios de casas",
        "n_muestras": n_muestras,
        "n_features": n_features
    }

    return info, X_df, y_series
