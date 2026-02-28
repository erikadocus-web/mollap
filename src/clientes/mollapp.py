class Mollapp:
    def __init__(self):
        self.programadorTareas = None
    
    def setProgramadorTareas(self, programadorTareas):
        self.programadorTareas = programadorTareas
    
    def enviarPeticion(self, id):
        self.programadorTareas.ejecutarTareas(id)