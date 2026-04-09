import numpy as np
import pandas as pd

def generar_datos_clientes(n_clientes=200):
    ingresos = np.random.randint(10000, 100000, n_clientes)
    puntuacion = np.random.randint(1, 101, n_clientes)

    datos = pd.DataFrame({
        "Ingreso_Anual": ingresos,
        "Puntuacion_Gasto": puntuacion
    })

    return datos

def generar_caso_de_uso_segmentacion_clientes():
    datos = generar_datos_clientes()

    etiquetas = np.random.randint(0, 3, len(datos))

    resultado = datos.copy()
    resultado["Cluster"] = etiquetas

    info = {
        "descripcion": "Segmentación de clientes basada en ingresos y puntuación de gasto",
        "n_clusters": 3
    }

    return info, resultado
