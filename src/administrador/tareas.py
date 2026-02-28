class Tareas():
    def __init__(self):
        self.listaTareas = []
        self.objetivo = None

    def getTareas(self):
        return self.listaTareas
    
    def getObjetivo(self):
        return self.objetivo
    
    def añadirTarea(self, tarea):
        self.listaTareas.append(tarea)
    
    def setObjetivo(self, objetivo):
        self.objetivo = objetivo

    def ejecutarTareas(self, mensaje):
        for tarea in self.listaTareas:
            tarea.ejecutar(mensaje)
        
        if self.objetivo:
            self.objetivo.ejecutar(mensaje)