class Tareas():
    def __init__(self):
        self.tareas = []
        self.objetivo = None

    def getTareas(self):
        return self.tareas
    
    def getObjetivo(self):
        return self.objetivo
    
    def getTarea(self,tarea):
        self.tareas.append(tarea)
    
    def setObjetivo(self, objetivo):
        self.objetivo = objetivo

    def ejecutarTareas(self, objetivo):
        for tarea in self.tareas:
            tarea.ejecutar(objetivo)
   