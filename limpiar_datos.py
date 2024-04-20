# Importar las librerías necesarias
import pandas as pd
import re


def limpiar_generos(lista_generos_str):
    """
    Esta función toma una cadena de texto que contiene información sobre los 
    géneros de una película. El texto está formado por una lista de géneros
    separados por comas. Esta función extrae los nombres de los géneros y
    los devuelve como una cadena separada por comas.
     -Ejemplo
    Entrada: "[{'id': 28, 'name': 'Action'}, {'id': 12, 'name': 'Adventure'}]"
    Salida: "Action, Adventure"
    
    Args:
        lista_generos_str (str): Cadena de texto que contiene información 
        sobre los géneros de una película.

    Returns:
        str: Cadena de texto que contiene los nombres de los géneros 
        separados por comas.
    """
    # Definir el patrón regex para capturar el texto después de 'name': '
    patron = r"'name': '([^']+)'"
    
    # Buscar todas las coincidencias del patrón en la cadena
    coincidencias = re.findall(patron, lista_generos_str)
    
    # Devolver los nombres de los géneros como una cadena separada por comas
    return str(", ".join(coincidencias))


def eliminar_no_ascii(texto):
    """
    Esta función toma un texto y lo convierte a ASCII.
    
    Args:
        texto (str): Texto a convertir.

    Returns:
        str: Texto convertido a ASCII.
    """
    return texto.encode('ascii', 'ignore').decode('ascii')


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
df_peliculas = df_relevante.dropna().astype(dtypes)

# Obtener la columna de géneros brutos
df_generos_brutos = df_peliculas['genres']

# Aplicar la función limpiar_generos a cada valor de la columna
df_peliculas['genres'] = df_generos_brutos.apply(limpiar_generos)

# Convertir la columna vote_average a entero multiplicando por 10
df_peliculas['vote_average'] = (df_peliculas['vote_average'] * 10).astype(int)

# Convertir la columna vote_count a entero
df_peliculas['vote_count'] = df_peliculas['vote_count'].astype(int)

# Convertir la columna popularity a entero
df_peliculas['popularity'] = df_peliculas['popularity'].astype(int)

# Eliminar filas con elementos vacíos
df_peliculas.dropna(inplace=True)

# Rellenar valores faltantes con ceros
df_peliculas.fillna(0, inplace=True)

# Eliminar caracteres no ASCII por cada columna del DataFrame
for columna in ['original_title', 'overview', 'genres']:
    df_peliculas[columna] = df_peliculas[columna].apply(eliminar_no_ascii)
    
# Escribir el nuevo archivo CSV
df_peliculas.to_csv("informacion_peliculas.csv", index=False)

