from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS pentru orice frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/recomanda")
async def recomanda(request: Request):
    data = await request.json()

    forma = data.get("formaFetei")
    gen = data.get("genul")
    stil = data.get("stilul")

    # Colectare masuratori numerice
    try:
        latime_fata = float(data.get("latimeFata", 0))
        inaltime_fata = float(data.get("inaltimeFata", 0))
        dist_ochi = float(data.get("distOchi", 0))
        latime_barbie = float(data.get("latimeBarbie", 0))
        raport = float(data.get("raport", 0))
        interpupilara = float(data.get("interpupilara", 0))
        latime_nas = float(data.get("latimeNas", 0))
        inaltime_frunte = float(data.get("inaltimeFrunte", 0))
        latime_sprancene = float(data.get("latimeSprancene", 0))
    except:
        return {"recomandare": "Datele primite nu au fost în format numeric valid."}

    # Analiză profesională
    analiza = f"""🔍 **Analiză facială**:
- Forma feței detectată: **{forma}**
- Raport lățime/înălțime: {raport:.2f}
- Distanță interpupilară: {interpupilara:.2f} px
- Lățime față: {latime_fata:.2f} px | Înălțime față: {inaltime_fata:.2f} px
- Lățime barbie: {latime_barbie:.2f} px | Lățime nas: {latime_nas:.2f} px
- Înălțime frunte: {inaltime_frunte:.2f} px | Lățime sprâncene: {latime_sprancene:.2f} px

👤 **Preferințe utilizator**:
- Gen: {gen}
- Stil preferat: {stil}
"""

    # Recomandare logică – ajustabilă după caz
    sugestii = ""

    # Recomandări în funcție de forma feței
    if forma == "Rotundă":
        sugestii += "- Alege rame pătrate sau dreptunghiulare care alungesc fața.\n"
        if stil == "Elegant":
            sugestii += "- Ramele subțiri din metal sau titan pot accentua rafinamentul.\n"
    elif forma == "Ovală":
        sugestii += "- Ai noroc! Forma feței tale permite aproape orice tip de rame.\n"
        if stil == "Casual":
            sugestii += "- Ramele din acetat colorat sau modele mai îndrăznețe pot fi o alegere bună.\n"
    elif forma == "Alungită":
        sugestii += "- Recomandăm rame mai înalte, rotunjite, care să echilibreze lungimea feței.\n"
        if stil == "Sport":
            sugestii += "- Ramele late, cu prindere bună și unghiuri curbate pot oferi și funcționalitate.\n"
    else:
        sugestii += "- Pentru forma feței tale, consultă un optician pentru o analiză personalizată.\n"

    # Ajustări în funcție de distanța interpupilară
    if interpupilara < 55:
        sugestii += "- Ai o distanță interpupilară mică, așa că rame înguste vor arăta mai bine.\n"
    elif interpupilara > 70:
        sugestii += "- O distanță interpupilară mare poate fi echilibrată cu rame largi.\n"

    # Construcția finală a răspunsului
    recomandare = f"""{analiza}

🎯 **Recomandare profesională**:
{suggestii.strip()}
"""

    return {"recomandare": recomandare}

