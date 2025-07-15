from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Activare CORS (pentru a permite frontendului accesul la backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/recomanda")
async def recomanda(data: Request):
    json_data = await data.json()

    formaFetei = json_data.get("formaFetei")
    genul = json_data.get("genul")
    stilul = json_data.get("stilul")
    latimeFata = json_data.get("latimeFata")
    inaltimeFata = json_data.get("inaltimeFata")
    distOchi = json_data.get("distOchi")
    latimeBarbie = json_data.get("latimeBarbie")
    raport = json_data.get("raport")
    interpupilara = json_data.get("interpupilara")
    latimeNas = json_data.get("latimeNas")
    inaltimeFrunte = json_data.get("inaltimeFrunte")
    latimeSprancene = json_data.get("latimeSprancene")

    # Recomandare exemplu simplificat
    recomandare = (
        f"Pentru o față {formaFetei}, gen {genul}, stil {stilul}, cu latime de {latimeFata} și raport {raport}, "
        f"se recomandă rame care echilibrează trăsăturile. Sugestie: rame ușoare, ovale sau dreptunghiulare, "
        f"cu punte nazală potrivită pentru o distanță interpupilară de {interpupilara}."
    )

    return {"raspuns": recomandare}

