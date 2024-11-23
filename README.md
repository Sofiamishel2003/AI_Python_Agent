Aquí tienes un archivo README.md estructurado para tu proyecto, ideal para subirlo a GitHub:

# Agente Interactivo con Streamlit y LangChain 🤖

Este proyecto implementa un agente interactivo utilizando Streamlit, LangChain y OpenAI, que responde preguntas basadas en **código Python** o en datos de archivos **CSV**. Los datos disponibles incluyen información sobre cetáceos, películas aclamadas, música de Billie Eilish y comida asiática. Además, el agente guarda un historial de preguntas y respuestas para consultas posteriores.
## Video de funcionamiento

## Características

- **Ejecución de código Python:** El agente puede escribir y ejecutar código Python para responder preguntas técnicas.
- **Análisis de CSV:** Responde preguntas basadas en datos de cuatro archivos CSV:
  - Cetáceos: Especies, longitud, peso, hábitat y dieta.
  - Películas aclamadas: Título, género, año, calificación IMDB y premios.
  - Música de Billie Eilish: Canciones, álbumes, género, año de lanzamiento y duración.
  - Comida asiática: Platillos, país de origen, ingredientes, tiempo de cocción y nivel de dificultad.
- **Historial de interacciones:** Guarda un registro de preguntas y respuestas en un archivo `history.txt`.

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/Sofiamishel2003/agente-interactivo.git
   cd agente-interactivo
   ```

2. Instala las dependencias requeridas:
   ```bash
   pip install -r requirements.txt
   ```

3. Asegúrate de tener un archivo `.env` con tu clave de OpenAI:
   ```
   OPENAI_API_KEY=tu_clave_de_api
   ```

4. Coloca los archivos CSV generados en la misma carpeta que este script:
   - `cetaceans_dataset_corrected.csv`
   - `acclaimed_movies_dataset_fixed.csv`
   - `billie_eilish_music_dataset.csv`
   - `asian_cooking_dataset.csv`

## Ejecución

1. Ejecuta la aplicación con Streamlit:
   ```bash
   streamlit run main.py
   ```

2. Abre el navegador en la URL proporcionada (generalmente `http://localhost:8501`).

## Video de demostración
Link to the video: [Video](https://youtu.be/bZE2xFX0glw)

### Ejecución de código Python
1. Selecciona uno de los ejemplos predefinidos en la sección **Python REPL**.
2. Haz clic en **Ejecutar Python** para obtener la respuesta generada por el agente.

### Consultas basadas en CSV
1. Escribe tu pregunta en el campo de texto debajo de **Interacción con archivos CSV**.
2. Haz clic en **Ejecutar pregunta** para obtener la respuesta.

### Ejemplos de preguntas
- **Cetáceos:** "¿Qué especies de cetáceos tienen una longitud mayor a 20 metros y dónde habitan?"
- **Películas aclamadas:** "¿Cuáles son las películas de género 'Drama' lanzadas después del año 2000 que tienen una calificación de IMDB mayor a 8.5?"
- **Música de Billie Eilish:** "¿Cuáles canciones del álbum 'Happier Than Ever' tienen una duración mayor a 3.5 minutos?"
- **Comida asiática:** "¿Qué platillos asiáticos tienen un nivel de dificultad 'Fácil' y tardan menos de 30 minutos en prepararse?"

## Archivos Incluidos

- `main.py`: Código principal del proyecto.
- `history.txt`: Archivo que almacena el historial de preguntas y respuestas.
- `requirements.txt`: Lista de dependencias necesarias.
- Archivos CSV:
  - `cetaceans_dataset_corrected.csv`
  - `acclaimed_movies_dataset_fixed.csv`
  - `billie_eilish_music_dataset.csv`
  - `asian_cooking_dataset.csv`

## Tecnologías Utilizadas

- **Streamlit**: Framework para crear interfaces web interactivas.
- **LangChain**: Herramienta para construir aplicaciones basadas en lenguaje natural.
- **OpenAI API**: Proporciona la funcionalidad de los modelos GPT.
- **Python**: Lenguaje principal del proyecto.

## Próximos pasos

- Integrar más datasets basados en otros temas de interés.
- Añadir soporte para gráficos interactivos basados en las respuestas.
- Mejorar la visualización del historial de preguntas y respuestas.

## Contribuciones

¡Contribuciones son bienvenidas! Por favor, abre un **issue** o crea un **pull request** para sugerir mejoras o reportar errores.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

🎉 ¡Gracias por usar este agente interactivo! Si tienes alguna duda o sugerencia, no dudes en abrir un issue.
```

