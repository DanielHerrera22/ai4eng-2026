import numpy as np
import pandas as pd

def generar_datos_clientes(n_clientes=200):
    # Ingreso anual entre 10k y 100k
    ingresos = np.random.randint(10000, 100000, n_clientes)

    # Puntuación de gasto entre 1 y 100
    puntuacion = np.random.randint(1, 101, n_clientes)

    # Crear DataFrame
    datos = pd.DataFrame({
        "Ingreso_Anual": ingresos,
        "Puntuacion_Gasto": puntuacion
    })

    return datos

datos = generar_datos_clientes()

etiquetas, centroides = segmentar_clientes_kmeans(datos, 3)
