import sqlite3


baglanti = sqlite3.connect("veritabani.db")
imlec = baglanti.cursor()


imlec.execute("""
CREATE TABLE IF NOT EXISTS masalar (
    ad TEXT PRIMARY KEY,
    yas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ad TEXT NOT NULL,
    yas INTEGER
)
""")


imlec.execute("INSERT INTO masalar (bos, dolu,rezerve) VALUES (?, ?,?)", ("Ahmet", 28))
baglanti.commit()


imlec.execute("SELECT * FROM masalar")
print(imlec.fetchall())

baglanti.close()
