from flask import Flask, jsonify, render_template, request
import sqlite3
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database.db")


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# =========================
# VISTA PRINCIPAL
# =========================
@app.route("/")
def index():
    return render_template("index.html")


# =========================
# CONSULTA DE PRECIO
# =========================
@app.route("/ver_precio", methods=["POST"])
def ver_precio():
    try:
        data = request.get_json()
        codigo = data.get("codigo")

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
