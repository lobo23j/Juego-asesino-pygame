import pygame

class Proyectil_asesino():
    def __init__(self, pantalla, configs, asesino):
        super(Proyectil_asesino, self).__init__()
        self.configs = configs
        self.pantalla = pantalla

        # Crea la imagen en (0,0) y luego establece la posición correcta
        self.imagen = self.imagen = pygame.image.load("imagenes/Estrella_ninja.png")
        self.imagen_redimensionada = pygame.transform.scale(self.imagen, (self.configs.tamaño_proyectil_asesino))
        self.rect = self.imagen_redimensionada.get_rect()
        self.rect.centerx = asesino.rect.centerx
        self.rect.centery = asesino.centery.nave

        # Almacena la posición de la bala como valor decimal
        self.y = float(self.rect.centery)
        self.x = float(self.rect.centerx)

        self.velocidad_bala = configs.velocidad_proyectil_asesino

    def update(self):
        """Mueve la bala hacia arriba en la pantalla"""
        # Actualiza la posición decimal de la bala
        self.y -= self.velocidad_bala
        # Actualiza la posición del rect
        self.rect.centery = self.y
        self.rect.centerx = self.x

    def blitme(self):
        """Dibuja al opbjeto en su ubicación actual"""
        self.pantalla.blit(self.imagen_redimensionada, self.rect)

