import pandas as pd
from cargar_datos import leer_datos_peliculas

df_peliculas = leer_datos_peliculas()

for pelicula in df_peliculas.head():
    print(f"Película: {pelicula}")
    print(f"Título: {pelicula.original_title}")
    print(f"Fecha de lanzamiento: {pelicula.release_date}")
