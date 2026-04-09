import numpy as np
import pandas as pd

def generar_datos_sensores(n_muestras=500, n_variables=50):
    datos = np.random.randn(n_muestras, n_variables) * 10 + 50
    return datos


def generar_caso_de_uso_reduccion_dimensionalidad():
    datos = generar_datos_sensores()

    n_componentes = 10 
    X_reducido = datos[:, :n_componentes]

    df_reducido = pd.DataFrame(X_reducido)

    info = {
        "descripcion": "Reducción de dimensionalidad en datos de sensores",
        "n_componentes": n_componentes
    }

    return info, df_reducido
