# Importaciones de bibliotecas
import os
from whoosh.fields import Schema, TEXT, NUMERIC, KEYWORD, DATETIME
from whoosh.analysis import StemmingAnalyzer
from whoosh.index import create_in, open_dir

# Importar función para cargar datos de películas desde CSV
from cargar_datos import leer_datos_peliculas  


# Cargar los datos de películas desde un archivo CSV
df_peliculas = leer_datos_peliculas()

# Definir el esquema del índice de búsqueda
schema = Schema(
    title=TEXT(stored=True),       
    overview=TEXT(stored=True, analyzer=StemmingAnalyzer()), 
    genres=KEYWORD(stored=True, commas=True, scorable=True),     
    popularity=NUMERIC(numtype=float, stored=True),  
    release_date=DATETIME(stored=True),  
    vote_average=NUMERIC(stored=True), 
    vote_count=NUMERIC(stored=True),
    )

# Crear irectorio donde se almacenará el índice de búsqueda si no existe
if not os.path.exists("indexdir"):
    # Crear el directorio para almacenar el índice de búsqueda
    os.mkdir("indexdir")
    
    # Crear el índice de búsqueda en el directorio con el esquema definido
    ix = create_in("indexdir", schema)

# Abrir el índice de búsqueda
ix = open_dir("indexdir")

# Obtener un writer para el índice de búsqueda
writer = ix.writer()

for pelicula in df_peliculas.itertuples():
    writer.add_document(
        title=pelicula.original_title,
        overview=pelicula.overview,
        genres=pelicula.genres,
        popularity=pelicula.popularity,
        release_date=pelicula.release_date,
        vote_average=pelicula.vote_average,
        vote_count=pelicula.vote_count,
    )

# Guardar los cambios en el índice de búsqueda
writer.commit()

