from zooAnimales.animal import Animal

class Ave(Animal):
    _listado = []
    _cantidadAv = 0
    halcones = 0
    aguilas = 0
    
    def __init__(self,nombre = "", edad = 0, habitat = "", genero = "", colorPlumas = ""):
        super().__init__(nombre,edad,habitat,genero)
        Ave._listado.append(self)
        self._colorPlumas = colorPlumas
        Ave._cantidadAv += 1
        
    def getColorPlumas(self):
        return self._colorPlumas
    
    def setColorPlumas(self,color):
        self._colorPlumas = color
    
    def movimiento(self) -> str:
        return "volar"
    
    @classmethod
    def cantidadAves(cls) -> int:
        return cls._cantidadAv
    
    @classmethod
    def getListado(cls):
        return cls._listado
    
    @classmethod
    def crearHalcon(cls,nombre = "", edad = 0, genero = ""):
        cls.halcones += 1
        halcon = Ave(nombre, edad, "montana", genero, "cafe glorioso")
        return halcon
        
    @classmethod
    def crearAguila(cls,nombre = "", edad = 0, genero = ""):
        cls.aguilas += 1
        aguila = Ave(nombre, edad, "montana", genero, "blanco y amarillo")
        return aguila