from .filtro import Filtro

class Autorizacion(Filtro):

    def ejecutar(self, mensaje):
        print(f"Autorizacion OK para {mensaje}")