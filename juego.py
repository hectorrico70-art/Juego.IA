"""
=========================================================
PROYECTO:
Piedra, Papel o Tijera con Inteligencia Artificial

Autor: Héctor Rico
Materia: Inteligencia Artificial y Sistemas Inteligentes
UNIMINUTO

Archivo:
juego.py

Descripción:
Contiene toda la lógica del juego.
Determina el ganador entre el jugador y la IA.
=========================================================
"""

# ============================================
# Movimientos válidos
# ============================================

MOVIMIENTOS = [
    "piedra",
    "papel",
    "tijera"
]

# ============================================
# Emojis para mostrar en pantalla
# ============================================

EMOJIS = {
    "piedra": "🪨 Piedra",
    "papel": "📄 Papel",
    "tijera": "✂️ Tijera"
}


# ============================================
# Verificar movimiento válido
# ============================================

def movimiento_valido(movimiento):
    """
    Retorna True si el movimiento existe.
    """

    return movimiento in MOVIMIENTOS


# ============================================
# Convertir movimiento a emoji
# ============================================

def convertir_emoji(movimiento):
    """
    Devuelve el nombre del movimiento con emoji.
    """

    return EMOJIS.get(
        movimiento,
        movimiento
    )


# ============================================
# Obtener resultado
# ============================================

def obtener_resultado(jugador, ia):
    """
    Determina el resultado del juego.

    Retorna:

    "Victoria"
    "Derrota"
    "Empate"
    """

    if not movimiento_valido(jugador):
        raise ValueError("Movimiento del jugador inválido.")

    if not movimiento_valido(ia):
        raise ValueError("Movimiento de la IA inválido.")

    # Empate

    if jugador == ia:
        return "Empate"

    # Casos donde gana el jugador

    if (

        (jugador == "piedra" and ia == "tijera")

        or

        (jugador == "papel" and ia == "piedra")

        or

        (jugador == "tijera" and ia == "papel")

    ):

        return "Victoria"

    # En cualquier otro caso gana la IA

    return "Derrota"


# ============================================
# Explicación del resultado
# ============================================

def descripcion_resultado(jugador, ia):
    """
    Devuelve una explicación textual
    del resultado.
    """

    if jugador == ia:
        return "Ambos eligieron el mismo movimiento."

    reglas = {

        ("piedra", "tijera"):
            "La piedra rompe la tijera.",

        ("tijera", "papel"):
            "La tijera corta el papel.",

        ("papel", "piedra"):
            "El papel envuelve la piedra.",

        ("tijera", "piedra"):
            "La piedra rompe la tijera.",

        ("papel", "tijera"):
            "La tijera corta el papel.",

        ("piedra", "papel"):
            "El papel envuelve la piedra."

    }

    return reglas.get(
        (jugador, ia),
        ""
    )


# ============================================
# Color para la interfaz
# ============================================

def color_resultado(resultado):
    """
    Devuelve el color correspondiente
    al resultado.
    """

    colores = {

        "Victoria": "verde",

        "Empate": "amarillo",

        "Derrota": "rojo"

    }

    return colores.get(
        resultado,
        "gris"
    )


# ============================================
# Icono del resultado
# ============================================

def icono_resultado(resultado):
    """
    Devuelve un emoji según el resultado.
    """

    iconos = {

        "Victoria": "🏆",

        "Empate": "🤝",

        "Derrota": "❌"

    }

    return iconos.get(
        resultado,
        "🎮"
    )


# ============================================
# Pruebas locales
# ============================================

if __name__ == "__main__":

    pruebas = [

        ("piedra", "tijera"),

        ("papel", "papel"),

        ("tijera", "piedra")

    ]

    print("=" * 50)
    print("PRUEBAS DEL MÓDULO JUEGO")
    print("=" * 50)

    for jugador, ia in pruebas:

        resultado = obtener_resultado(
            jugador,
            ia
        )

        print()

        print(
            convertir_emoji(jugador),
            "vs",
            convertir_emoji(ia)
        )

        print(
            "Resultado:",
            resultado
        )

        print(
            descripcion_resultado(
                jugador,
                ia
            )
        )

    print("\nPruebas finalizadas correctamente.")
