from django.shortcuts import render
from django.http.response import HttpResponseNotFound
from transformers import TextGenerationPipeline, GPT2LMHeadModel, AutoTokenizer
from translate import Translator
from dotenv import dotenv_values

# Create your views here.
def index(request):
    return render(request, "core/index.html")

def generar_historia(genre):
    model_name = "aspis/gpt2-genre-story-generation"

    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    generator = TextGenerationPipeline(model=model, tokenizer=tokenizer)
    input_prompt = f"<BOS> <{genre}>"
    story = generator(input_prompt, max_length=400, do_sample=True,repetition_penalty=1.5, temperature=1.2, 
                top_p=0.95, top_k=50)
    
    return story

def arreglar_historia(historia):
    nueva_historia = ""
    historia = historia.split()

    for i in range(2, len(historia)):
        if i != 2:
            nueva_historia += " "
        nueva_historia += historia[i]

    return nueva_historia

def traducir_texto(texto_ingles):
    translator = Translator(from_lang='en', to_lang='es')
    max_chars = 500  # Máximo de caracteres permitidos por la biblioteca

    # Divide el texto en segmentos de máximo 500 caracteres
    segmentos = [texto_ingles[i:i+max_chars] for i in range(0, len(texto_ingles), max_chars)]

    # Traduce cada segmento y almacena las traducciones
    traducciones = []
    for segmento in segmentos:
        traduccion_segmento = translator.translate(segmento)
        traducciones.append(traduccion_segmento)

    # Une las traducciones para obtener el texto completo traducido
    texto_espanol = ' '.join(traducciones)

    return texto_espanol


def generate_story(request):
    if request.method == 'POST':
        genres = ["romance", "adventure", "mystery-&-detective", "fantasy", "humor-&-comedy", "paranormal", "science-fiction"]
        generos = ["romance", "aventura", "misterio", "fantasia", "comedia", "paranormal", "ciencia-ficcion"]
        mapa = {generos[i]:genres[i] for i in range(len(generos))}

        data = request.POST
        genre = data["genre"]

        if genre not in mapa:
            return HttpResponseNotFound("Por favor digita bien el género, dirigete al index nuevamente")

        historia = generar_historia(mapa[genre])
        historia = historia[0]["generated_text"]
        historia = arreglar_historia(historia)
        historia = traducir_texto(historia)
        

    return render(request, "core/index.html", context={"historia": historia})