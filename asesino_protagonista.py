import time

import pygame

from funciones_juego import actualizar_pantalla

from funciones_juego import verificar_eventos

class Asesino():
    """Sirve para gestionar el comportamiento de el asesino principal"""

    def __init__(self, configs, pantalla, plataforma1, plataforma2, plataforma3):
        """Inicializa el personaje y establece su punto de partida"""

        self.pantalla = pantalla
        self.configs = configs
        self.plataforma1 = plataforma1
        self.plataforma2 = plataforma2
        self.plataforma3 = plataforma3

        # Carga la imagen del personaje y obtiene su rect(rectángulo)
        self.imagen = pygame.image.load("imagenes/rogue/idle/idle1.png")
        self.imagen_redimensionada = pygame.transform.scale(self.imagen,(self.configs.tamaño_asesino))
        self.rect = self.imagen_redimensionada.get_rect()
        self.pantalla_rect = pantalla.get_rect()

        # Empieza de nuevo en el mismo lugar
        self.rect.centerx = 130
        self.rect.centery = 300

        # Almacena valor decimal para centro del asesino
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # Banderas de movimiento
        self.mover_asesino_derecha = False
        self.mover_asesino_izquierda = False
        self.saltar_asesino = False
        self.caer_asesino = False
        self.respawn_asesino = False
        self.ataque_basico_asesino = False
        self.direccion_asesino = "Neutro"
        self.salto_lateral_derecha = False
        self.salto_lateral_izquierda = False

        self.lista_correr_asesino = ["Imagenes/Rogue/Run/run1.png","Imagenes/Rogue/Run/run2.png","Imagenes/Rogue/Run/run3.png","Imagenes/Rogue/Run/run4.png","Imagenes/Rogue/Run/run5.png","Imagenes/Rogue/Run/run6.png","Imagenes/Rogue/Run/run7.png","Imagenes/Rogue/Run/run8.png",]
        self.lista_saltar_asesino = ["Imagenes/Rogue/Jump/jump1.png","Imagenes/Rogue/Jump/jump2.png","Imagenes/Rogue/Jump/jump3.png","Imagenes/Rogue/Jump/jump4.png","Imagenes/Rogue/Jump/jump5.png","Imagenes/Rogue/Jump/jump6.png","Imagenes/Rogue/Jump/jump7.png"]
        self.lista_ataque_basico_asesino = ["Imagenes/Rogue/Attack/Attack1.png", "Imagenes/Rogue/Attack/Attack2.png", "Imagenes/Rogue/Attack/Attack3.png", "Imagenes/Rogue/Attack/Attack4.png", "Imagenes/Rogue/Attack/Attack5.png", "Imagenes/Rogue/Attack/Attack6.png", "Imagenes/Rogue/Attack/Attack7.png"]

    def update(self):
        """Actualiza la poscición del asesino según las banderas de movimiento"""

        # Movimiento hacia la derecha del asesino
        if self.mover_asesino_derecha == True and self.rect.centerx + 40 < self.pantalla_rect.right:
            for andar_animacion_derecha in self.lista_correr_asesino:
                if self.mover_asesino_derecha == False:# or self.rect.centerx + 40 < self.pantalla_rect.right:
                    break
                self.imagen = pygame.image.load(andar_animacion_derecha)
                self.imagen_redimensionada = pygame.transform.scale(self.imagen, (self.configs.tamaño_asesino))
                self.centerx += self.configs.velocidad_movimiento_asesino
                self.rect.centerx = self.centerx
                actualizar_pantalla(self.pantalla, self, self.plataforma1, self.plataforma2, self.plataforma3)
                verificar_eventos(self, self.plataforma1, self.plataforma2, self.plataforma3, self.pantalla)
            self.direccion_asesino = "Derecha"

        print(self.direccion_asesino)

        # Movimiento hacia la izquierda del asesino
        if self.mover_asesino_izquierda  == True and self.rect.centerx - 40 > self.pantalla_rect.left:
            #self.centerx -= 20
            self.rect.centerx = self.centerx
            for andar_animacion_izquierda in self.lista_correr_asesino:
                if self.mover_asesino_izquierda == False:# or self.rect.centerx + 40 < self.pantalla_rect.right:
                    break
                self.imagen = pygame.image.load(andar_animacion_izquierda)
                self.imagen_redimensionada = pygame.transform.scale(self.imagen, (self.configs.tamaño_asesino))
                self.imagen_girada =  pygame.transform.flip(self.imagen_redimensionada, True, False)
                self.imagen_redimensionada = self.imagen_girada
                self.centerx -= self.configs.velocidad_movimiento_asesino
                self.rect.centerx = self.centerx
                actualizar_pantalla(self.pantalla, self, self.plataforma1, self.plataforma2, self.plataforma3)
                verificar_eventos(self, self.plataforma1, self.plataforma2, self.plataforma3, self.pantalla)
            # self.centerx += 20
            self.rect.centerx = self.centerx
            actualizar_pantalla(self.pantalla, self, self.plataforma1, self.plataforma2, self.plataforma3)
            self.direccion_asesino = "Izquierda"
        print(self.direccion_asesino)

        # Salto del asesino hacia la derecha
        if self.salto_lateral_derecha == True:
            self.imagen = pygame.image.load("Imagenes/Rogue/Jump/jump5.png")
            self.imagen_redimensionada = pygame.transform.scale(self.imagen, (self.configs.tamaño_asesino))
            actualizar_pantalla(self.pantalla, self, self.plataforma1, self.plataforma2, self.plataforma3)
            self.centery -= self.configs.tamaño_salto_asesino
            self.centerx += self.configs.salto_lateral_asesino
            self.rect.centery = self.centery
            self.rect.centerx = self.centery
            actualizar_pantalla(self.pantalla, self, self.plataforma1, self.plataforma2, self.plataforma3)
            time.sleep(0.5)
            self.imagen = pygame.image.load("Imagenes/Rogue/Jump/jump6.png")
            self.imagen_redimensionada = pygame.transform.scale(self.imagen, (self.configs.tamaño_asesino))
            actualizar_pantalla(self.pantalla, self, self.plataforma1, self.plataforma2, self.plataforma3)
            self.centery += self.configs.tamaño_salto_asesino
            while self.caer_asesino == False:
                self.centerx += self.configs.salto_lateral_asesino
                self.rect.centerx = self.centerx
            self.rect.centery = self.centery
            self.rect.centerx = self.centerx
            actualizar_pantalla(self.pantalla, self, self.plataforma1, self.plataforma2, self.plataforma3)

        # Salto del asesino hacia la izquierda
        if self.salto_lateral_izquierda == True:
            self.rect.centery = self.centery
            self.rect.centerx = self.centery
            self.imagen = pygame.image.load("Imagenes/Rogue/Jump/jump6.png")
            self.imagen_redimensionada = pygame.transform.scale(self.imagen, (self.configs.tamaño_asesino))
            self.imagen_girada = pygame.transform.flip(self.imagen_redimensionada, True, False)
            self.imagen_redimensionada = self.imagen_girada
            actualizar_pantalla(self.pantalla, self, self.plataforma1, self.plataforma2, self.plataforma3)
            self.centery -= self.configs.tamaño_salto_asesino
            self.centerx -= self.configs.salto_lateral_asesino
            self.rect.centery = self.centery
            self.rect.centerx = self.centery
            actualizar_pantalla(self.pantalla, self, self.plataforma1, self.plataforma2, self.plataforma3)
            time.sleep(0.1)
            self.centery += self.configs.tamaño_salto_asesino
            self.centerx -= self.configs.salto_lateral_asesino
            self.rect.centery = self.centery
            self.rect.centerx = self.centerx
            actualizar_pantalla(self.pantalla, self, self.plataforma1, self.plataforma2, self.plataforma3)

        # Salto en vertical
        if self.saltar_asesino == True:
            self.imagen = pygame.image.load("Imagenes/Rogue/Jump/jump1.png")
            self.imagen_redimensionada = pygame.transform.scale(self.imagen, (self.configs.tamaño_asesino))
            actualizar_pantalla(self.pantalla, self, self.plataforma1, self.plataforma2, self.plataforma3)
            self.centery -= self.configs.tamaño_salto_asesino
            self.rect.centery = self.centery
            actualizar_pantalla(self.pantalla, self, self.plataforma1, self.plataforma2, self.plataforma3)
            time.sleep(0.1)
            self.centery += self.configs.tamaño_salto_asesino
            self.rect.centery = self.centery
            actualizar_pantalla(self.pantalla, self, self.plataforma1, self.plataforma2, self.plataforma3)

        # Ataque básico del asesino hacia la derecha
        if self.ataque_basico_asesino == True and self.direccion_asesino == "Derecha":
            for ataque_simple_asesino in self.lista_ataque_basico_asesino:
                self.imagen = pygame.image.load(ataque_simple_asesino)
                self.imagen_redimensionada = pygame.transform.scale(self.imagen, (self.configs.tamaño_asesino))
                actualizar_pantalla(self.pantalla, self, self.plataforma1, self.plataforma2, self.plataforma3)

        # Ataque básico del asesino hacia la izquierda
        if self.ataque_basico_asesino == True and self.direccion_asesino == "Izquierda":
            for ataque_simple_asesino_izquierda in self.lista_ataque_basico_asesino:
                self.imagen = pygame.image.load(ataque_simple_asesino_izquierda)
                self.imagen_redimensionada = pygame.transform.scale(self.imagen, (self.configs.tamaño_asesino))
                self.imagen_girada =  pygame.transform.flip(self.imagen_redimensionada, True, False)
                self.imagen_redimensionada = self.imagen_girada
                actualizar_pantalla(self.pantalla, self, self.plataforma1, self.plataforma2, self.plataforma3)
            self.rect.centerx = self.centerx
            self.rect.centery = self.centery

        # Cambiar de imagen cuando para de moverse hacia la derecha
        while self.mover_asesino_derecha == False and self.mover_asesino_izquierda == False and self.saltar_asesino == False and self.respawn_asesino == False and self.caer_asesino == True and self.ataque_basico_asesino == False and self.direccion_asesino == "Derecha" and self.salto_lateral_derecha == False and self.salto_lateral_izquierda == False:
            """Para de moverse hacia la derecha"""
            self.imagen = pygame.image.load("Imagenes/Rogue/Walk/walk6.png")
            self.imagen_redimensionada = pygame.transform.scale(self.imagen, (self.configs.tamaño_asesino))
            actualizar_pantalla(self.pantalla, self, self.plataforma1, self.plataforma2, self.plataforma3)
            for i in range(1,5):
                time.sleep(0.2)
                verificar_eventos(self, self.plataforma1, self.plataforma2, self.plataforma3, self.pantalla)
                if self.mover_asesino_derecha == True or self.mover_asesino_izquierda == True or self.saltar_asesino == True or self.respawn_asesino == True or self.caer_asesino == False or self.ataque_basico_asesino == True or self.salto_lateral_derecha == True or self.salto_lateral_izquierda == True:
                    break
            while True:
                self.imagen = pygame.image.load("Imagenes/Rogue/Idle/idle1.png")
                self.imagen_redimensionada = pygame.transform.scale(self.imagen, (self.configs.tamaño_asesino))
                actualizar_pantalla(self.pantalla, self, self.plataforma1, self.plataforma2, self.plataforma3)
                verificar_eventos(self, self.plataforma1, self.plataforma2, self.plataforma3, self.pantalla)
                if self.mover_asesino_derecha == True or self.mover_asesino_izquierda == True or self.saltar_asesino == True or self.respawn_asesino == True or self.caer_asesino == False or self.ataque_basico_asesino == True or self.salto_lateral_derecha == True or self.salto_lateral_izquierda == True:
                    break
                self.rect.centerx = self.centerx
                self.rect.centery = self.centery
            # self.direccion_asesino= "Neutro"
        print(self.direccion_asesino)

        # Parar de moverse hacia la izquierda
        while self.mover_asesino_derecha == False and self.mover_asesino_izquierda == False and self.saltar_asesino == False and self.respawn_asesino == False and self.caer_asesino == True and self.ataque_basico_asesino == False and self.direccion_asesino == "Izquierda" and self.salto_lateral_derecha == False and self.salto_lateral_izquierda == False:
            """Para de moverse hacia la izquierda"""
            self.imagen = pygame.image.load("Imagenes/Rogue/Walk/walk6.png")
            self.imagen_redimensionada = pygame.transform.scale(self.imagen, (self.configs.tamaño_asesino))
            self.imagen_girada = pygame.transform.flip(self.imagen_redimensionada, True, False)
            self.imagen_redimensionada = self.imagen_girada
            actualizar_pantalla(self.pantalla, self, self.plataforma1, self.plataforma2, self.plataforma3)
            for i in range(1,5):
                time.sleep(0.2)
                verificar_eventos(self, self.plataforma1, self.plataforma2, self.plataforma3, self.pantalla)
                if self.mover_asesino_derecha == True or self.mover_asesino_izquierda == True or self.saltar_asesino == True or self.respawn_asesino == True or self.caer_asesino == False or self.ataque_basico_asesino == True or self.salto_lateral_derecha == True or self.salto_lateral_izquierda == True:
                    break
            while True:
                self.imagen = pygame.image.load("Imagenes/Rogue/Idle/idle1.png")
                self.imagen_redimensionada = pygame.transform.scale(self.imagen, (self.configs.tamaño_asesino))
                actualizar_pantalla(self.pantalla, self, self.plataforma1, self.plataforma2, self.plataforma3)
                verificar_eventos(self, self.plataforma1, self.plataforma2, self.pantalla, self.plataforma3)
                if self.mover_asesino_derecha == True or self.mover_asesino_izquierda == True or self.saltar_asesino == True or self.respawn_asesino == True or self.caer_asesino == False or self.ataque_basico_asesino == True or self.salto_lateral_derecha == True or self.salto_lateral_izquierda == True:
                    break
                self.rect.centerx = self.centerx
                self.rect.centery = self.centery
            # self.direccion_asesino = "Neutro"

        # Caída del asesino porque no está en contacto con la plataforma
        if self.caer_asesino == False and self.rect.bottom < self.pantalla_rect.bottom:
            self.centery += 50
            self.rect.centery = self.centery

        # Para volver a la posición incial del juego
        if self.respawn_asesino == True:
            self.imagen = pygame.image.load("Imagenes/Rogue/Idle/idle1.png")
            self.centerx = 130
            self.rect.centerx = self.centerx
            self.centery = 250
            self.rect.centery = self.centery
            actualizar_pantalla(self.pantalla, self, self.plataforma1, self.plataforma2, self.plataforma3)

        # Actualiza el objeto rect desde self.center
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """Dibuja al asesino en su ubicación actual"""
        self.pantalla.blit(self.imagen_redimensionada, self.rect)

