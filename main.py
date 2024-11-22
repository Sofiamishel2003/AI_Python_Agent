import os
import datetime
from typing import Any, Dict

import streamlit as st
from dotenv import load_dotenv
from langchain import hub
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain_experimental.tools import PythonREPLTool
from langchain_experimental.agents.agent_toolkits import create_csv_agent

load_dotenv()


def save_history(question, answer):
    with open("history.txt", "a") as f:
        f.write(f"{datetime.datetime.now()}: {question}-->{answer}\n")


def load_history():
    if os.path.exists("history.txt"):
        with open("history.txt", "r") as f:
            return f.readlines()
    return []


def main():
    st.set_page_config(page_title="Agente Interactivo", page_icon="🤖", layout="wide")

    st.title("🤖 Agente Interactivo")
    st.markdown("### Descripción del Bot")
    st.markdown("""
    Este bot tiene la capacidad de ejecutar código Python para responder preguntas y también de responder preguntas basadas en datos de diferentes archivos CSV. 
    Utiliza el input para escribir preguntas específicas o selecciona una de las opciones para ejecutar ejemplos predefinidos.
    """)

    instructions = """You are an agent designed to write and execute python code to answer questions.
    You have access to a python REPL, which you can use to execute python code.
    You have qrcode package installed.
    If you get an error, debug your code and try again.
    Only use the output of your code to answer the question.
    You might know the answer without running any code, but you should still run the code to get the answer.
    If it does not seem like you can write code to answer the question, just return "I don't know" as the answer.
    """

    base_prompt = hub.pull("langchain-ai/react-agent-template")
    prompt = base_prompt.partial(instructions=instructions)

    tools = [PythonREPLTool()]
    python_agent = create_react_agent(
        prompt=prompt,
        llm=ChatOpenAI(temperature=0, model="gpt-4o"),
        tools=tools,
    )

    python_agent_executor = AgentExecutor(agent=python_agent, tools=tools, verbose=True)

    # Definición de agentes para cada archivo CSV
    cetaceans_agent = create_csv_agent(
        llm=ChatOpenAI(temperature=0, model="gpt-4"),
        path="cetaceans_dataset.csv",
        verbose=True,
        allow_dangerous_code=True,
    )
    movies_agent = create_csv_agent(
        llm=ChatOpenAI(temperature=0, model="gpt-4"),
        path="acclaimed_movies_dataset.csv",
        verbose=True,
        allow_dangerous_code=True,
    )
    music_agent = create_csv_agent(
        llm=ChatOpenAI(temperature=0, model="gpt-4"),
        path="billie_eilish_music_dataset.csv",
        verbose=True,
        allow_dangerous_code=True,
    )
    cooking_agent = create_csv_agent(
        llm=ChatOpenAI(temperature=0, model="gpt-4"),
        path="asian_cooking_dataset.csv",
        verbose=True,
        allow_dangerous_code=True,
    )

    def python_agent_executor_wrapper(original_prompt: str) -> dict[str, Any]:
        return python_agent_executor.invoke({"input": original_prompt})

    # Wrappers for each CSV agent
    def cetaceans_agent_wrapper(input_prompt: str) -> dict[str, Any]:
        return cetaceans_agent.invoke({"input": input_prompt})

    def movies_agent_wrapper(input_prompt: str) -> dict[str, Any]:
        return movies_agent.invoke({"input": input_prompt})

    def music_agent_wrapper(input_prompt: str) -> dict[str, Any]:
        return music_agent.invoke({"input": input_prompt})

    def cooking_agent_wrapper(input_prompt: str) -> dict[str, Any]:
        return cooking_agent.invoke({"input": input_prompt})

    tools = [
        Tool(name="Python Agent", func=python_agent_executor_wrapper,
             description="""Useful when you need to transform natural language to python and execute the python code, 
             returning the results of the code execution DOES NOT ACCEPT CODE AS INPUT"""),
        Tool(name="Cetaceans Data Agent", func=cetaceans_agent_wrapper,
             description="Provides detailed answers about cetaceans, including species, size, weight, habitat, and diet, "
                         "based on cetaceans_dataset_corrected.csv."),
        Tool(name="Acclaimed Movies Agent", func=movies_agent_wrapper,
             description="Provides insights about critically acclaimed movies, including year, genre, IMDB rating, and awards, "
                         "based on acclaimed_movies_dataset_fixed.csv."),
        Tool(name="Billie Eilish Music Agent", func=music_agent_wrapper,
             description="Answers questions about Billie Eilish's music, including song titles, albums, release year, genre, "
                         "and duration, based on billie_eilish_music_dataset.csv."),
        Tool(name="Asian Cooking Agent", func=cooking_agent_wrapper,
             description="Provides information about Asian dishes, including origin, ingredients, cooking time, and difficulty, "
                         "based on asian_cooking_dataset.csv."),
    ]

    prompt = base_prompt.partial(instructions="")
    grand_agent = create_react_agent(
        prompt=prompt,
        llm=ChatOpenAI(temperature=0, model="gpt-4-turbo"),
        tools=tools
    )

    grand_agent_executor = AgentExecutor(
        agent=grand_agent,
        tools=tools,
        verbose=True,
    )

    # Interfaz de Streamlit

    # Sección de Python REPL
    st.markdown("## Python REPL")
    python_options = [
        "La división de los números 4000 sobre 40",
        "Simula el lanzamiento de dos dados 500 veces y calcula la probabilidad de obtener un total de 7",
        "Genera un patrón piramidal de asteriscos de tamaño 5",
    ]
    python_example = st.selectbox("Ejemplos de Python", python_options, key="python_example")
    if st.button("Ejecutar Python", key="execute_python"):
        loading_placeholder = st.empty()
        loading_placeholder.markdown("### Procesando tu respuesta...")

        try:
            response = python_agent_executor_wrapper(python_example)
            if 'output' in response:
                st.markdown("### Respuesta del agente:")
                st.code(response['output'], language="python")
                save_history(python_example, response['output'])
            else:
                st.error("No hubo salida del agente.")
        except Exception as e:
            st.error(f"Error al ejecutar el agente: {str(e)}")

    st.markdown("---")  # Separador

    # Sección de Interacción con archivos CSV
    st.markdown("## Interacción con archivos CSV")
    st.markdown("### Descripción de los archivos CSV disponibles")
    st.markdown("""
        - **cetaceans_dataset_corrected.csv**: Información sobre cetáceos, incluyendo especie, longitud, peso, hábitat y dieta.
        - **acclaimed_movies_dataset_fixed.csv**: Detalles sobre películas aclamadas, incluyendo título, género, año, calificación IMDB y premios.
        - **billie_eilish_music_dataset.csv**: Información sobre música de Billie Eilish, como canciones, álbumes, géneros, año de lanzamiento y duración.
        - **asian_cooking_dataset.csv**: Detalles sobre comida asiática, como platillos, país de origen, ingredientes principales, tiempo de cocción y nivel de dificultad.
        """)

    csv_question = st.text_input("Escribe tu pregunta", key="csv_input")
    if st.button("Ejecutar pregunta", key="execute_query"):
        loading_placeholder = st.empty()
        loading_placeholder.markdown("### Procesando tu respuesta...")
        try:
            response = grand_agent_executor.invoke({"input": csv_question})
            if 'output' in response:
                st.markdown("### Respuesta del agente:")
                st.write(response['output'])
                save_history(csv_question, response['output'])
            else:
                st.error("No se pudo obtener una respuesta adecuada para la pregunta.")
        except Exception as e:
            st.error(f"Error al procesar la pregunta: {str(e)}")

    st.markdown("## Historial")
    if st.button("Cargar Historial", key="load_history"):
        history = load_history()
        for entry in history:
            st.text(entry)

    st.write("")
    st.write("")


if __name__ == "__main__":
    main()