from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permite CORS pentru orice origine (pentru test)
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
    gen = json_data.get("genul")
    stil = json_data.get("stilul")

    # Exemplu simplificat de logică
    recomandare = f"Pentru o față {forma}, gen {gen}, stil {stil}, recomandăm rame subțiri, ovale."
    return {"raspuns": recomandare}
