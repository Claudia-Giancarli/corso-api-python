from fastapi import FastAPI,HTTPException
import sqlite3

app= FastAPI()



@app.get("/utente")
def root():
    return {"nome ": "Claudia", "Cognome": "Giancarli"}
    
@app.get ("/saluta/{nome}")
def saluta_utente(nome: str):
    return{"messaggio": f"Ciao {nome}!"}
 #URL :/saluta/Mario
 #output: {"messaggio": "ciao Mario"}
         
@app.get ("/ricerca")
def cerca(item: str,q: int=1):
    return {"risultato": item,  "quantita":q}
# URL :/ricerca?item=mela&q=5
#output: {"risultato": "mela","quantita":5}

@app.get("/somma/{n1}/{n2}")
def som(  n1: int , n2: int):
    if (n1==1 and n2==1):
        raise HTTPException(status_code=400, detail="operazione non valida")
    return{"risultato": f"{n1+n2}"}

#url:/somma?item=n1&n2=valore
#output:{"risultato": "valore": }

@app.get("/prodotti")
def ottieni_prodotti():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row # Conversione attiva!
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM prodotti")
    risultato = cursor.fetchall()
    conn.close()
    return risultato