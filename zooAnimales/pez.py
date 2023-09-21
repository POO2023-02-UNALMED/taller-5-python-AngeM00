from zooAnimales.animal import Animal

class Pez(Animal):
    _listado = []
    _cantidadP = 0
    salmones = 0
    bacalaos = 0
    
    def __init__(self,nombre = "", edad = 0, habitat = "", genero = "", colorEscamas = "", cantidadAletas=0):
        super().__init__(nombre,edad,habitat,genero)
        Pez._listado.append(self)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez._cantidadP += 1
        
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, color):
        self._colorEscamas = color
        
    def getCantidadAletas(self):
        return self._cantidadAletas
    
    def setCantidadAletas(self,cantidad):
        self._cantidadAletas = cantidad
        
    def movimiento(self) -> str:
        return "nadar"
    
    @classmethod
    def cantidadPeces(cls) -> int:
        return cls._cantidadP
    
    @classmethod
    def getListado(cls):
        return cls._listado
    
    @classmethod
    def crearSalmon(cls,nombre = "", edad = 0, genero = ""):
        cls.salmones += 1
        salmon = Pez(nombre,edad,"oceano",genero,"rojo",6)
        return salmon
    
    @classmethod
    def crearBacalao(cls,nombre = "", edad = 0, genero = ""):
        cls.bacalaos += 1
        bacalao = Pez(nombre,edad,"oceano",genero,"gris",6)
        return bacalao