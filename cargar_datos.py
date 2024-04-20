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
        # Leer los datos del archivo CSV
        datos = pd.read_csv('informacion_peliculas.csv')
        
        # Eliminar los valores nulos
        datos.dropna(inplace=True)
        
        # Devolver los datos
        return datos
    except FileNotFoundError:
        # Imprimir un mensaje de error si no se encuentra el archivo
        print("El archivo CSV no se encontró en la ruta especificada.")
        
        # Si no se encuentra el archivo, devolver None
        return None


if __name__ == "__main__":
    # Leer los datos del archivo CSV
    df_peliculas = leer_datos_peliculas()
    df_peliculas.dropna(inplace=True)
    #print(df_peliculas.info())
    #print(df_peliculas.head())
    filas_con_nan = df_peliculas[df_peliculas.isna().any(axis=1)]
    print(filas_con_nan)
