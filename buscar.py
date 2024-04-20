# Importar librerías necesarias
import streamlit as st
from whoosh.qparser import MultifieldParser
from whoosh.index import open_dir

# Definir la página web
# Establecer el título de la página web
st.header("Motor de búsqueda de películas")

# Mostrar un mensaje de bienvenida
st.write("""Ingrese el nombre de una película (hecha entre 1995 y 2017) 
         para buscar información sobre ella.""")

# Definir los campos en los que deseas buscar coincidencias
campos_busqueda = ["title", "overview", "release_date"]

# Abrir el índice de búsqueda
ix = open_dir("indexdir")

# Crear un objeto MultifieldParser para buscar en múltiples campos
qp = MultifieldParser(campos_busqueda, schema=ix.schema)

# Mostrar la interfaz de búsqueda y guardar su resultado
query = st.text_input("Ingrese la película que desea buscar:")

# Buscar la película en la base de datos si se ha ingresado una consulta
if query:
    with ix.searcher() as searcher:
        try:
            # Utilizar el MultifieldParser para buscar en múltiples campos
            resultados = searcher.search(qp.parse(query))
        except Exception as e:
            # Manejar errores de tiempo de ejecución
            st.error(f"""Algo ha fallado.\nError: {e}""")
            
            # No mostrar resultados si la búsqueda tarda demasiado o falla
            resultados = None
        
        # Imprimir la información de cada resultado
        # Mostrar los resultados si se encontraron coincidencias
        if resultados:
            # Mostrar un mensaje de confirmación con la cantidad de resultados
            st.success(f"Se encontraron {len(resultados)} resultados.")
            # Mostrar los resultados en una tabla
            for i, resultado in enumerate(resultados):
                st.markdown(f"## :movie_camera: Resultado {i+1} :clapper:")
                st.write("**Título:**", resultado['title'])
                st.write("**Descripción:**", resultado['overview'])
                st.write("**Géneros:**", resultado['genres'])
                st.write("**Índice de popularidad:**", resultado['popularity'])
                st.write("**Fecha de lanzamiento:**", resultado['release_date'])
                st.write("**Puntuación:**", resultado['vote_average'], "%")
                st.write("**Votos:**", resultado['vote_count'])
                st.write("---")
        else:
            # Mostrar un mensaje de error si no se encontraron resultados
            st.error("""No se encontraron resultados. 
                    Por favor, intente con otra consulta.""")
