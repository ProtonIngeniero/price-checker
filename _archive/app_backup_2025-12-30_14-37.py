from flask import Flask, jsonify, send_from_directory
import sqlite3
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database.db")

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    return send_from_directory(BASE_DIR, "index.html")

# 🔹 SERVIR LOGO EXPLÍCITAMENTE
@app.route("/logo_doremi.png")
def logo():
    return send_from_directory(BASE_DIR, "logo_doremi.png")

@app.route("/precio/<codigo>")
def precio(codigo):
    try:
        conn = get_db()
        cur = conn.cursor()

        cur.execute(
            "SELECT nombre, precio FROM productos WHERE codigo = ?",
            (codigo,)
        )

        row = cur.fetchone()
        conn.close()

        if row:
            return jsonify({
                "nombre": row["nombre"],
                "precio": row["precio"]
            })
        else:
            return jsonify({"error": "Producto no registrado"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
