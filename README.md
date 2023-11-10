# Generador de historias cortas usando IA

## Arquitectura
1. Python
2. Modelos pre-entrenados con GPT2.
3. Bases de datos de hugging face.
4. Para la aplicación web, se usa Django.

## Librerías
1. Transformers
2. Translate
3. Django

## Cómo ejecutar la aplicación?
### Pre requisitos
1. Tener Python instalado con una versión 3.8+.
2. Tener pip instalado.

### Paso a paso
1. Clonar este mismo repositorio.
2. Instalar Django con `pip install django`
3. Instalar Transformers y optimum (hace parte de transformers) `pip3 install transformers optimum`
4. Instalar dependencia gpt `pip install auto-gptq --extra-index-url https://huggingface.github.io/autogptq-index/whl/cu118/`
5. Instalar translate `pip install translate`
6. Una vez clonado el repositorio, debemos ubicarnos dentro de la carpeta del repositorio usando una terminal.
7. Una vez ahí, ejecutar el comando: `cd story_generator`.
8. Una vez ejecutado el comando, ejectura `python3 manage.py runserver`
9. Y listo! Abre el servidor local en tu navegador: `http://127.0.0.1:8000/`
