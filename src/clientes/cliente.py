class Cliente:
    def setProgramadorTareas(self, programadorTareas):
        self.programadorTareas = programadorTareas
    
    def enviarPeticion(self, peticion):
        self.programadorTareas.ejecutarTareas(peticion)