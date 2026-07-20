/*
=========================================================
PROYECTO:
Piedra, Papel o Tijera con Inteligencia Artificial

Archivo:
script.js

Autor:
Héctor Rico

Descripción:
Animaciones y efectos visuales.
=========================================================
*/

document.addEventListener("DOMContentLoaded", () => {

    console.log("Proyecto iniciado correctamente.");

    // ================================
    // Animar barra de aprendizaje
    // ================================

    const barra = document.querySelector(".progreso");

    if (barra) {

        const ancho = barra.style.width;

        barra.style.width = "0%";

        setTimeout(() => {

            barra.style.width = ancho;

        }, 300);

    }

    // ================================
    // Animación de botones
    // ================================

    const botones = document.querySelectorAll(".btn");

    botones.forEach((boton) => {

        boton.addEventListener("mouseenter", () => {

            boton.style.transform = "scale(1.08)";

        });

        boton.addEventListener("mouseleave", () => {

            boton.style.transform = "";

        });

    });

    // ================================
    // Resaltar resultado
    // ================================

    const resultado = document.querySelector(".resultado");

    if (resultado) {

        resultado.animate(

            [

                {
                    transform: "scale(0.9)",
                    opacity: 0
                },

                {
                    transform: "scale(1)",
                    opacity: 1
                }

            ],

            {

                duration: 600

            }

        );

    }

    // ================================
    // Confirmar reinicio
    // ================================

    const reinicio = document.querySelector(".btn-reiniciar");

    if (reinicio) {

        reinicio.addEventListener("click", function (e) {

            const respuesta = confirm(
                "¿Deseas reiniciar todas las estadísticas?"
            );

            if (!respuesta) {

                e.preventDefault();

            }

        });

    }

    // ================================
    // Resaltar filas del historial
    // ================================

    const filas = document.querySelectorAll("tbody tr");

    filas.forEach((fila) => {

        fila.addEventListener("mouseenter", () => {

            fila.style.background = "rgba(255,255,255,.18)";

        });

        fila.addEventListener("mouseleave", () => {

            fila.style.background = "";

        });

    });

    // ================================
    // Mostrar mensaje según resultado
    // ================================

    if (resultado) {

        const titulo = resultado.querySelector("h2");

        if (titulo) {

            const texto = titulo.textContent;

            if (texto.includes("Victoria")) {

                console.log("¡Ganaste!");

            }

            else if (texto.includes("Derrota")) {

                console.log("La IA ganó esta ronda.");

            }

            else {

                console.log("Empate.");

            }

        }

    }

    // ================================
    // Scroll suave
    // ================================

    document.documentElement.style.scrollBehavior = "smooth";

});
