# [BuscaTuPelicula 🔍](https://buscatupelicula.streamlit.app/)

## ¿Qué es? 🤔
El Motor de Búsqueda de Películas es una herramienta poderosa diseñada para facilitar la búsqueda y el descubrimiento de películas dentro de una extensa base de datos de más de 42,000 películas. Desarrollado utilizando Python, este proyecto aprovecha las bibliotecas Pandas y Whoosh para ofrecer una experiencia de búsqueda eficiente y precisa.

## Características Principales ✔️
1. **Amplia Base de Datos:** Con más de 42,000 películas en la base de datos, los usuarios tienen acceso a una amplia variedad de títulos para explorar.
2. **Búsqueda Eficiente:** Gracias a la implementación de Whoosh, el motor de búsqueda proporciona resultados rápidos y precisos, incluso con grandes volúmenes de datos.
3. **Funcionalidades Avanzadas:** Los usuarios pueden realizar búsquedas para obtener datos de películas incluyendo información adicional, como sinopsis, año de lanzamiento, géneros y calificaciones.
4. **Interfaz Intuitiva:** La interfaz de usuario es fácil de usar y ofrece una experiencia fluida de navegación para los usuarios.

## Tecnologías Utilizadas ⚡
- Python: Lenguaje de programación principal utilizado para el desarrollo del proyecto.
- Pandas: Biblioteca de Python utilizada para la manipulación y análisis de datos.
- Whoosh: Motor de búsqueda de texto completo implementado para proporcionar funcionalidades de búsqueda avanzadas.
- Streamlit: Biblioteca de Python y servicio web para el diseño y desarrollo de aplicaciones.

## Futuras Mejoras 🔜
1. **Registro de usuarios** Implementar el registro de usuarios para almacenar sus gustos, preferencias, e información de otras funcionalidades.
2. **Funciones de recomendación** Incluir busqueda de resultados basados en la popularidad de las peliculas y los géneros asociados al usuario y a la película.
3. **Ampliación de la base de datos** Obtener datos de las películas en otros idiomas y conseguir datos más recientes.
4. **Personalización:** Crear una función donde los usuarios pueden guardar sus búsquedas favoritas, crear listas de peliculas por ver.

## ¿Cómo Funciona?
- Se limpió la información obtenida de [The Movies Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset) de [Kaggle](https://www.kaggle.com/), que contenía alrededor de 45.000 filas. Después de la limpieza y la organización de los datos se obtuvieron 42.000 filas no nulas. Hecho en limpiar_datos.py. Se crea un nuevo dataframe después de limpiar los datos y se crea el *.csv con la información.
- El archivo cargar_datos.py se encarga de leer y cargar el *.csv a un dataframe de Pandas
- Con Whoosh se creó un esquema para almacenar la información de cada documento/película, luego se indexaron con indexar.py dentro de la carpeta indexdir.
- La vista de la aplicación se define en buscar.py con la librería de Streamlit. Se importa Whoosh para leer el directorio indexdir y la película ingresada por el usuario procede a buscarse.

Con el Motor de Búsqueda de Películas, los amantes del cine pueden explorar títulos de su interés de manera rápida y conveniente. Este proyecto demuestra mis habilidades en el desarrollo de aplicaciones de búsqueda utilizando Python y herramientas como Pandas y Whoosh.

