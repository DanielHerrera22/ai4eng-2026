import numpy as np
import pandas as pd

def generar_datos_fraude(n_muestras=1000, n_features=10, ratio_fraude=0.05):
    X = np.random.randn(n_muestras, n_features)

    y = np.zeros(n_muestras)
    n_fraudes = int(n_muestras * ratio_fraude)

    indices_fraude = np.random.choice(n_muestras, n_fraudes, replace=False)
    y[indices_fraude] = 1

    return X, y


def generar_caso_de_uso_deteccion_fraude():
    X, y = generar_datos_fraude()

    score = np.random.uniform(0.7, 0.95)

    df = pd.DataFrame(X)
    df["fraude"] = y

    info = {
        "descripcion": "Evaluación de detección de fraude en transacciones",
        "metodo": "validacion_cruzada_simulada",
        "score_promedio": float(score)
    }

    return info, df
