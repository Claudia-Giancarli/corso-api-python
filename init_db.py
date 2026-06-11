
import sqlite3

from fastapi import FastAPI
app=FastAPI
conn = sqlite3.connect("database.db")
cursor = conn.cursor()
cursor.execute("""
       CREATE TABLE IF NOT EXISTS prodotti (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
             prezzo REAL
)
""")
lista_prodotti = [
    ("Mouse Wireless", 25.50),
    ("Tastiera Meccanica", 89.90),
    ("Monitor 24 Pollici", 149.00),
    ("Cuffie Gaming", 45.00),
    ("Tappetino XL", 15.00)
]
cursor.executemany("INSERT INTO prodotti (nome, prezzo) VALUES (?, ?)", lista_prodotti)

@app.get("/prodotti")
def ottieni_prodotti():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row # Conversione attiva!
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM prodotti")
    risultato = cursor.fetchall()
    conn.close()
    return risultato
@app.get("/prodotti/ricerca")
def cerca_prodotto(keyword: str):
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM prodotti WHERE nome LIKE ?",
        (f"%{keyword}%",)
)
    risultati = cursor.fetchall()
    conn.close()
    return risultati


conn.commit()
conn.close()