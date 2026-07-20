"""
=========================================================
PROYECTO:
Piedra, Papel o Tijera con Inteligencia Artificial

Archivo:
estadisticas.py

Descripción:
Gestiona todas las estadísticas de la partida.

Autor:
Héctor Rico
=========================================================
"""


class Estadisticas:

    def __init__(self):

        self.reiniciar()

    # ==========================================

    def actualizar(self, jugador, ia, resultado):

        self.partidas += 1

        if resultado == "Victoria":

            self.victorias += 1

            self.puntaje += 3

        elif resultado == "Empate":

            self.empates += 1

            self.puntaje += 1

        else:

            self.derrotas += 1

        self.historial.insert(0, {

            "numero": self.partidas,

            "jugador": jugador,

            "ia": ia,

            "resultado": resultado

        })

    # ==========================================

    def porcentaje_victorias(self):

        if self.partidas == 0:

            return 0

        return round(

            (self.victorias / self.partidas) * 100,

            1

        )

    # ==========================================

    def porcentaje_empates(self):

        if self.partidas == 0:

            return 0

        return round(

            (self.empates / self.partidas) * 100,

            1

        )

    # ==========================================

    def porcentaje_derrotas(self):

        if self.partidas == 0:

            return 0

        return round(

            (self.derrotas / self.partidas) * 100,

            1

        )

    # ==========================================

    def mejor_resultado(self):

        if self.victorias >= self.empates and self.victorias >= self.derrotas:

            return "Victorias"

        elif self.empates >= self.derrotas:

            return "Empates"

        else:

            return "Derrotas"

    # ==========================================

    def reiniciar(self):

        self.partidas = 0

        self.victorias = 0

        self.empates = 0

        self.derrotas = 0

        self.puntaje = 0

        self.historial = []


# ==============================================
# PRUEBAS
# ==============================================

if __name__ == "__main__":

    estadisticas = Estadisticas()

    estadisticas.actualizar(

        "piedra",

        "tijera",

        "Victoria"

    )

    estadisticas.actualizar(

        "papel",

        "papel",

        "Empate"

    )

    estadisticas.actualizar(

        "tijera",

        "piedra",

        "Derrota"

    )

    print("=" * 50)

    print("ESTADÍSTICAS")

    print("=" * 50)

    print("Partidas:", estadisticas.partidas)

    print("Victorias:", estadisticas.victorias)

    print("Empates:", estadisticas.empates)

    print("Derrotas:", estadisticas.derrotas)

    print("Puntaje:", estadisticas.puntaje)

    print()

    print("Historial")

    print()

    for partida in estadisticas.historial:

        print(partida)
