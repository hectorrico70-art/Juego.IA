from flask import Flask, render_template, request

from juego import (
    obtener_resultado,
    convertir_emoji,
    descripcion_resultado,
    color_resultado,
    icono_resultado
)

from ia import IA
from estadisticas import Estadisticas

app = Flask(__name__)

# ===========================
# Objetos globales
# ===========================

ia = IA()
estadisticas = Estadisticas()


@app.route("/", methods=["GET", "POST"])
def inicio():

    datos = {

        "jugador": None,
        "ia": None,
        "resultado": None,
        "descripcion": "",
        "color": "gris",
        "icono": "🎮",
        "razon": "",

        "jugador_emoji": "",
        "ia_emoji": "",

        "victorias": estadisticas.victorias,
        "empates": estadisticas.empates,
        "derrotas": estadisticas.derrotas,
        "puntaje": estadisticas.puntaje,
        "partidas": estadisticas.partidas,

        "historial": estadisticas.historial,

        "aprendizaje": ia.porcentaje_aprendizaje(),
        "movimiento_favorito": ia.movimiento_favorito()

    }

    if request.method == "POST":

        # Reiniciar

        if request.form.get("accion") == "reiniciar":

            estadisticas.reiniciar()

            ia.reiniciar()

            return render_template(

                "index.html",

                **datos

            )

        # Jugada del usuario

        jugador = request.form["jugada"]

        movimiento_ia, razon = ia.jugar()

        resultado = obtener_resultado(

            jugador,

            movimiento_ia

        )

        descripcion = descripcion_resultado(

            jugador,

            movimiento_ia

        )

        color = color_resultado(

            resultado

        )

        icono = icono_resultado(

            resultado

        )

        ia.aprender(

            jugador

        )

        estadisticas.actualizar(

            jugador,

            movimiento_ia,

            resultado

        )

        datos = {

            "jugador": jugador,

            "ia": movimiento_ia,

            "resultado": resultado,

            "descripcion": descripcion,

            "color": color,

            "icono": icono,

            "razon": razon,

            "jugador_emoji": convertir_emoji(jugador),

            "ia_emoji": convertir_emoji(movimiento_ia),

            "victorias": estadisticas.victorias,

            "empates": estadisticas.empates,

            "derrotas": estadisticas.derrotas,

            "puntaje": estadisticas.puntaje,

            "partidas": estadisticas.partidas,

            "historial": estadisticas.historial,

            "aprendizaje": ia.porcentaje_aprendizaje(),

            "movimiento_favorito": ia.movimiento_favorito()

        }

    return render_template(

        "index.html",

        **datos

    )


if __name__ == "__main__":

    app.run(

        debug=True

    )
