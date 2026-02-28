class ProgramadorTareas:
    def __init__(self, objetivo):
        self.tareas = Tareas()
        self.tareas.setObjetivo(objetivo)
    
    def añadirTareas(self, tarea):
        self.tareas.añadirTarea(tarea)
    
    def setTareas(self, tareas):
        self.tareas = tareas
    
    def ejecutarTareas(self, mensaje):
        self.tareas.ejecutarTareas(mensaje)
    