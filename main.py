from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/recomanda")
async def recomanda(data: Request):
    json_data = await data.json()

    forma = json_data.get("formaFetei")
    genul = json_data.get("genul")
    stilul = json_data.get("stilul")
    latimeFata = float(json_data.get("latimeFata", 0))
    inaltimeFata = float(json_data.get("inaltimeFata", 0))
    distOchi = float(json_data.get("distOchi", 0))
    latimeBarbie = float(json_data.get("latimeBarbie", 0))
    raport = float(json_data.get("raport", 1))
    interpupilara = float(json_data.get("interpupilara", 0))
    latimeNas = float(json_data.get("latimeNas", 0))
    inaltimeFrunte = float(json_data.get("inaltimeFrunte", 0))
    latimeSprancene = float(json_data.get("latimeSprancene", 0))

    recomandari = []

    # Reguli generale după formă
    if forma == "Rotundă":
        recomandari.append("rame pătrate sau dreptunghiulare pentru a adăuga unghiuri feței")
    elif forma == "Ovală":
        recomandari.append("aproape orice formă se potrivește, dar evită ramele prea mari")
    elif forma == "Alungită":
        recomandari.append("rame mai înalte, cu lentile ovale sau rotunde, care echilibrează lungimea")

    # Lățime față
    if latimeFata < 100:
        recomandari.append("ramele înguste sunt mai potrivite pentru fețele mici")
    elif latimeFata > 160:
        recomandari.append("alege rame late pentru a echilibra proporțiile")

    # Interpupilară
    if interpupilara < 60:
        recomandari.append("evită punțile nazale foarte largi")
    elif interpupilara > 70:
        recomandari.append("alege rame cu punte mai lată pentru confort vizual")

    # Stil preferat
    if stilul == "Elegant":
        recomandari.append("recomandăm rame metalice subțiri, aurii sau argintii")
    elif stilul == "Casual":
        recomandari.append("rame din acetat, în culori calde sau naturale")
    elif stilul == "Sport":
        recomandari.append("rame ușoare, curbate, din materiale rezistente")

    # Genul (ca accent, nu diferență radicală)
    if genul == "Feminin":
        recomandari.append("poți încerca și rame cu design delicat, pastel sau cat-eye")
    elif genul == "Masculin":
        recomandari.append("forme clasice precum pătrate sau dreptunghiulare, în culori neutre")

    mesaj_final = " ".join(recomandari)
    return {"raspuns": mesaj_final}

