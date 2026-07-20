"""
=========================================================
PROYECTO:
Piedra, Papel o Tijera con Inteligencia Artificial

Archivo:
ia.py

Descripción:
Implementa una IA basada en reconocimiento de patrones.
Analiza las jugadas del usuario y aprende cuál movimiento
utiliza con mayor frecuencia.
=========================================================
"""

import random
from collections import Counter


class IA:

    def __init__(self):

        self.historial = []

        self.movimientos = [

            "piedra",

            "papel",

            "tijera"

        ]

    # ----------------------------------------

    def reiniciar(self):

        self.historial.clear()

    # ----------------------------------------

    def aprender(self, movimiento):

        self.historial.append(movimiento)

    # ----------------------------------------

    def jugar(self):

        """
        Devuelve:

        movimiento_ia

        explicacion
        """

        # Primeras partidas

        if len(self.historial) < 5:

            movimiento = random.choice(self.movimientos)

            return (

                movimiento,

                "Primeras partidas: la IA juega aleatoriamente para recopilar información."

            )

        # Analizar patrones

        conteo = Counter(self.historial)

        mas_usado = conteo.most_common(1)[0][0]

        # Contrarrestar

        if mas_usado == "piedra":

            return (

                "papel",

                "La IA detectó que normalmente juegas Piedra y eligió Papel para contrarrestarte."

            )

        elif mas_usado == "papel":

            return (

                "tijera",

                "La IA detectó que normalmente juegas Papel y eligió Tijera para contrarrestarte."

            )

        else:

            return (

                "piedra",

                "La IA detectó que normalmente juegas Tijera y eligió Piedra para contrarrestarte."

            )

    # ----------------------------------------

    def porcentaje_aprendizaje(self):

        """
        Calcula el progreso del aprendizaje.

        Máximo 100%.
        """

        porcentaje = len(self.historial) * 20

        return min(porcentaje, 100)

    # ----------------------------------------

    def movimiento_favorito(self):

        if len(self.historial) == 0:

            return "Sin datos"

        conteo = Counter(self.historial)

        return conteo.most_common(1)[0][0]

    # ----------------------------------------

    def total_jugadas(self):

        return len(self.historial)


# =============================================
# Prueba del módulo
# =============================================

if __name__ == "__main__":

    ia = IA()

    pruebas = [

        "piedra",

        "piedra",

        "papel",

        "piedra",

        "tijera",

        "piedra",

        "papel"

    ]

    for movimiento in pruebas:

        ia.aprender(movimiento)

    print("=" * 50)

    print("INTELIGENCIA ARTIFICIAL")

    print("=" * 50)

    print("Historial:")

    print(ia.historial)

    print()

    print("Movimiento favorito:")

    print(ia.movimiento_favorito())

    print()

    movimiento, razon = ia.jugar()

    print("IA juega:")

    print(movimiento)

    print()

    print("Razón:")

    print(razon)

    print()

    print("Aprendizaje:")

    print(f"{ia.porcentaje_aprendizaje()} %")
