import sys

import pygame

def verificar_eventos_keydown(event, asesino, pantalla):
    """Responde a las pulsaciones de las teclas"""
    if event.key == pygame.K_SPACE:
        if asesino.direccion_asesino == "Derecha":
            asesino.salto_lateral_derecha = True
        elif asesino.direccion_asesino == "Izquierda":
            asesino.salto_lateral_izquierda = True
        elif asesino.direccion_asesino == "Neutro":
            asesino.saltar_asesino = True
        else:
            print("Error 00")
            sys.exit()
    if event.key == pygame.K_RIGHT:
        asesino.mover_asesino_derecha = True
    if event.key == pygame.K_LEFT:
        asesino.mover_asesino_izquierda = True
    if event.key == pygame.K_e:
        asesino.ataque_basico_asesino = True
    if event.key == pygame.K_BACKSPACE:
        asesino.respawn_asesino = True
    if event.key == pygame.K_TAB:
        pantalla.cambio_fondo = True

def verificar_eventos_keyup(event, asesino):
    if event.key == pygame.K_SPACE:
        asesino.salto_lateral_derecha = False
    if event.key == pygame.K_SPACE:
        asesino.salto_lateral_izquierda = False
    if event.key == pygame.K_RIGHT:
        asesino.mover_asesino_derecha = False
    if event.key == pygame.K_LEFT:
        asesino.mover_asesino_izquierda = False
    if event.key == pygame.K_SPACE:
        asesino.saltar_asesino = False
    if event.key == pygame.K_BACKSPACE:
        asesino.respawn_asesino = False
    if event.key == pygame.K_e:
        asesino.ataque_basico_asesino = False

def verificar_choques(asesino, plataforma1, plataforma2, plataforma3):
    if asesino.rect.colliderect(plataforma1.rect) == True or\
            asesino.rect.colliderect(plataforma2.rect) == True or\
            asesino.rect.colliderect(plataforma3.rect) == True:
        asesino.caer_asesino = True
    else:
        asesino.caer_asesino = False


def verificar_eventos(asesino, plataforma1, plataforma2, plataforma3, pantalla):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            verificar_eventos_keydown(event, asesino, pantalla)

        elif event.type == pygame.KEYUP:
            verificar_eventos_keyup(event, asesino)

    verificar_choques(asesino, plataforma1, plataforma2, plataforma3)


def actualizar_pantalla(pantalla, asesino, plataforma1, plataforma2, plataforma3):
    """Actualiza las imágenes en la pantalla y pasa a la siguiente pantalla"""

    fondo = pygame.image.load("imagenes/game_background_1.png")
    pantalla.blit(fondo, (0, 0))

    plataforma1.blitme()
    plataforma2.blitme()
    plataforma3.blitme()
    asesino.blitme()

    # Hace visible la pantalla más reciente
    pygame.display.flip()

def pantalla_inicial(pantalla):
    fondo1 = pygame.image.load("imagenes/pantalla_inicial_juego.bmp")
    pantalla.blit(fondo1, (0, 0))

    pygame.display.flip()

