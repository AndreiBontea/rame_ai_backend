from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# Activare CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/recomanda")
async def recomanda(request: Request):
    data = await request.json()

    formaFetei = data.get("formaFetei")
    genul = data.get("genul")
    stilul = data.get("stilul")
    latimeFata = data.get("latimeFata")
    inaltimeFata = data.get("inaltimeFata")
    distOchi = data.get("distOchi")
    latimeBarbie = data.get("latimeBarbie")
    raport = data.get("raport")
    interpupilara = data.get("interpupilara")
    latimeNas = data.get("latimeNas")
    inaltimeFrunte = data.get("inaltimeFrunte")
    latimeSprancene = data.get("latimeSprancene")

    prompt = f"""
Ești un consultant profesionist în optică și stil facial. Primești date extrem de detaliate despre trăsăturile faciale ale unui client, cu scopul de a recomanda un model de rame de ochelari perfect adaptat.

Clientul are următoarele caracteristici:
- Gen: {genul}
- Stil preferat: {stilul}
- Formă generală a feței: {formaFetei}

Vectori faciali măsurați:
- Lățime față: {latimeFata}
- Înălțime față: {inaltimeFata}
- Raport lățime/înălțime: {raport}
- Distanță între ochi: {distOchi}
- Distanță interpupilară: {interpupilara}
- Lățime bărbie: {latimeBarbie}
- Lățime nas: {latimeNas}
- Înălțime frunte: {inaltimeFrunte}
- Lățime sprâncene: {latimeSprancene}

✅ Ține cont de toate aceste măsurători. Analizează proporțiile și echilibrul feței.
✅ Nu oferi o recomandare generală — ci una **personalizată exclusiv pe baza valorilor primite**.
✅ Recomandarea trebuie să aibă 4–6 fraze, să includă explicații clare și să fie exprimată profesionist, dar accesibil pentru client.

Răspuns:
"""

    try:
        completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{ "role": "user", "content": prompt }],
            temperature=0.6,
        )
        rezultat = completion["choices"][0]["message"]["content"]
        return { "recomandare": rezultat }

    except Exception as e:
        print("Eroare OpenAI:", e)
        return { "recomandare": "Eroare la generarea recomandării." }
