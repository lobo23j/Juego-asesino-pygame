class Configuraciones:
    """Almacena todas las configuraciones del juego"""

    def __init__(self):
        """Inicia las configuraciones del juego"""

        # Tamaño pantalla
        self.pantalla_ancho = 1280
        self.pantalla_alto = 1024

        #Color pantalla
        self.pantalla_color = 125, 245, 234

        # Características asesino
        self.velocidad_movimiento_asesino = 10
        self.tamaño_salto_asesino = 100
        self.tamaño_asesino = 60, 80
        self.salto_lateral_asesino = 50

        # Características proyectil asesino
        self.tamaño_proyectil_asesino = 40, 40
        self.velocidad_proyectil_asesino = 20

