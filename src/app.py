# Importamos lo necesario para nuestra página web
from flask import Flask, request, render_template
import pickle
from pathlib import Path

# Creamos nuestra aplicación
app = Flask(__name__)

# Cargamos el modelo de flores que ya entrenamos
ruta = Path(__file__).resolve().parent.parent / "models" / "modelo_iris.pkl"

with open(ruta, "rb") as archivo:
    modelo = pickle.load(archivo)

# Nombres de las flores
especies = {
    0: "Iris setosa",
    1: "Iris versicolor",
    2: "Iris virginica"
}

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None

    if request.method == "POST":
        # Recogemos las cuatro medidas
        medidas = [
            float(request.form["val1"]),
            float(request.form["val2"]),
            float(request.form["val3"]),
            float(request.form["val4"])
        ]

        # Predecimos la especie
        prediccion = modelo.predict([medidas])[0]
        resultado = especies[prediccion]

    return render_template("index.html", prediction=resultado)
