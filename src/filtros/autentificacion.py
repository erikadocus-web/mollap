from .filtro import Filtro

class Autentificacion(Filtro):
    def ejecutar(self, mensaje):
        print(f"Autenticacion OK para {mensaje}")