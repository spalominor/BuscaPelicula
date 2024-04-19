# Importar las librerías necesarias
import pandas as pd

# Cargar el archivo CSV original
df = pd.read_csv("movies_metadata.csv")

# Seleccionar columnas relevantes
columnas_relevantes = ['original_title', 
                    'overview', 
                    'genres', 
                    'popularity', 
                    'release_date', 
                    'vote_average', 
                    'vote_count']

# Crear un nuevo DataFrame con las columnas relevantes
df_relevante = df[columnas_relevantes]

# Especifica los tipos de datos de cada columna
dtypes = {
    'original_title': 'str',
    'overview': 'str',
    'genres': 'str',
    'popularity': 'float',
    'release_date': 'str',
    'vote_average': 'float',
    'vote_count': 'float',
}


# Leer el archivo CSV filtrado y eliminar filas con valores faltantes
df_peliculas = pd.read_csv("informacion_peliculas.csv").dropna()

# Escribir el nuevo archivo CSV
df_peliculas.to_csv("informacion_peliculas.csv", index=False)

