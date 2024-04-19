# Importaciones de bibliotecas
import streamlit as st
from whoosh.fields import Schema, TEXT, NUMERIC
from whoosh.index import create_in, open_dir
from whoosh.qparser import QueryParser

# Importar función para cargar datos de películas desde CSV
from cargar_datos import leer_datos_peliculas  


# Cargar los datos de películas desde un archivo CSV
df_peliculas = leer_datos_peliculas()

# Definir el esquema del índice de búsqueda
schema = Schema(
    title=TEXT(stored=True),       # Título de la película
    overview=TEXT(stored=True),    # Descripción de la película
    genres=TEXT(stored=True),      # Géneros de la película
    popularity=NUMERIC(float, stored=True),    # Popularidad de la película
    release_date=TEXT(stored=True),            # Fecha de lanzamiento de la película
    vote_average=NUMERIC(float, stored=True),  # Promedio de votos de la película
    vote_count=NUMERIC(float, stored=True)     # Recuento de votos de la película
)

# Directorio donde se almacenará el índice de búsqueda
index_dir = "movie_index"

# Crear el índice de búsqueda en el directorio especificado con el esquema definido
index = create_in(index_dir, schema)

# Obtener un writer para el índice de búsqueda
with index.writer() as writer:
    # Iterar sobre las filas del DataFrame y agregar cada película al índice
    for _, row in df_peliculas.iterrows():
        writer.add_document(
            title=row['original_title'],
            overview=row['overview'],
            genres=row['genres'],
            popularity=row['popularity'],
            release_date=row['release_date'],
            vote_average=row['vote_average'],
            vote_count=row['vote_count']
        )
        
# Abrir el índice de búsqueda
index = open_dir(index_dir)

# Crear un parser de consultas para el campo de búsqueda 'overview'
qp = QueryParser("overview", schema=index.schema)

# Definir la interfaz de usuario con Streamlit
st.title("Motor de Búsqueda de Películas")

# Campo de entrada para que los usuarios ingresen sus consultas de búsqueda
query = st.text_input("Ingrese el título de la película que desea buscar:")

# Botón para iniciar la búsqueda
if st.button("Buscar"):
    # Parsear la consulta del usuario
    q = qp.parse(query)

    # Realizar la búsqueda en el índice
    with index.searcher() as searcher:
        results = searcher.search(q)

    # Mostrar los resultados de la búsqueda
    if len(results) > 0:
        st.write(f"Se encontraron {len(results)} resultados:")
        for i, result in enumerate(results[:10]):
            st.write(f"""- Título: {result['title']},
                     Descripción: {result['overview']},
                     Géneros: {result['genres']},
                     Popularidad: {result['popularity']},
                     Fecha de lanzamiento: {result['release_date']},
                     Calificación promedio: {result['vote_average']},
                     """)
            if i == 22:
                st.write("...")
                break
    else:
        st.write("No se encontraron resultados para la consulta ingresada.")