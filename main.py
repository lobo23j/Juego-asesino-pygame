import pygame

from configuraciones import Configuraciones

import funciones_juego as fj

from asesino_protagonista import Asesino

from plataforma_tierra import Plataforma_de_tierra

from pantalla import Pantalla

from proyectil_asesino import Proyectil_asesino

def run_game():
    """Inicia el juego y crea un objeto pantalla"""

    pygame.init()
    configs = Configuraciones()
    pantalla = pygame.display.set_mode((configs.pantalla_ancho, configs.pantalla_alto))
    pygame.display.set_caption("Juego1")
    pantalla_fondo = Pantalla()
    clock = pygame.time.Clock()

    # Crea al personaje asesino
    plataforma1 = Plataforma_de_tierra(pantalla, 130, 350)
    plataforma2 = Plataforma_de_tierra(pantalla, 300, 700)
    plataforma3 = Plataforma_de_tierra(pantalla, 400, 650)
    asesino = Asesino(configs, pantalla, plataforma1, plataforma2, plataforma3)

    # Crea un grupo para almacenar las plataformas
    Plataformas = (plataforma1, plataforma2, plataforma3)

    while True:
        fj.verificar_eventos(asesino, plataforma1, plataforma2, plataforma3, pantalla_fondo)
        fj.pantalla_inicial(pantalla)
        if pantalla_fondo.cambio_fondo == True:
            while True:
                fj.verificar_eventos(asesino, plataforma1, plataforma2, plataforma3, pantalla_fondo)
                asesino.update()
                fj.actualizar_pantalla(pantalla, asesino, plataforma1, plataforma2, plataforma3)
                clock.tick(10)
                print(asesino.direccion_asesino)

run_game()
