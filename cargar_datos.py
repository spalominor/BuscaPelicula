# Importar las liberías necesarias
import pandas as pd

def leer_datos_peliculas():
    """
    Lee los datos del archivo CSV con la información de las películas
    y devuelve un DataFrame de pandas.

    Args:
    ruta_archivo (str): La ruta del archivo CSV.

    Returns:
    pd.DataFrame: Un DataFrame de pandas con los datos del archivo CSV.
    """
    try:
        datos = pd.read_csv('informacion_peliculas.csv')
        return datos
    except FileNotFoundError:
        print("El archivo CSV no se encontró en la ruta especificada.")
        return None


if __name__ == "__main__":
    # Leer los datos del archivo CSV
    df_peliculas = leer_datos_peliculas()
    print(df_peliculas.info())
