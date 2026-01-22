import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS tiendas (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    pin TEXT
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS productos (
    codigo TEXT PRIMARY KEY,
    nombre TEXT,
    precio INTEGER,
    tienda_id INTEGER,
    FOREIGN KEY(tienda_id) REFERENCES tiendas(id)
)
""")

c.execute("INSERT OR IGNORE INTO tiendas VALUES (1,'Doremi Centro','4321')")
c.execute("INSERT OR IGNORE INTO productos VALUES ('7801234567890','Arroz Grade A 1 KG',1290,1)")

conn.commit()
conn.close()

print("Base de datos creada correctamente")

