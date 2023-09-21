class Zona:
    def __init__(self, nombre = "", zoologico=None, animales = None):
        self._nombre = nombre
        self._zoo = zoologico
        self._animales = animales
        
    def getNombre(self) -> str:
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getZoo(self):
        return self._zoo
    
    def setZoo(self, zoo):
        if self._zoo == None:
            self._zoo = []
        self._zoo.append(zoo)
        
    def agregarAnimales(self,animal) -> None:
        if self._animales == None:
            self._animales = []
            
        self._animales.append(animal)
        
    def cantidadAnimales(self) -> int:
        if self._animales == None:
            cantidad = 0
        else:
            cantidad = len(self._animales)
        return cantidad