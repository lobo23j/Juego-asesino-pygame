import pygame.image


class Plataforma_de_tierra():
    """Crea la clase de las plataformas de tipo tierra"""

    def __init__(self, pantalla, cordenadax, cordenaday):
        """Inicia la plataforma y pone su punto de partida"""

        self.pantalla = pantalla

        # Carga la imagen de la plataforma y obtiene su rect
        self.imagen = pygame.image.load("imagenes/pads/Pad_1_3.png")
        self.imagen_redimensionada = pygame.transform.scale(self.imagen, (190, 40))
        self.rect = self.imagen_redimensionada.get_rect()

        # Empieza siempre en el mismo lugar
        self.rect.centerx = cordenadax
        self.rect.centery = cordenaday

    def blitme(self):
        """Dibuja la plataforma en su ubicación actual"""
        self.pantalla.blit(self.imagen_redimensionada, self.rect)
