from zooAnimales.animal import Animal

class Reptil(Animal):
    _listado = []
    _cantidadR = 0
    iguanas = 0
    serpientes = 0
    
    def __init__(self,nombre = "", edad = 0, habitat = "", genero = "", colorEscamas = "", largo=0):
        super().__init__(nombre,edad,habitat,genero)
        Reptil._listado.append(self)
        self._colorEscamas = colorEscamas
        self._largoCola = largo
        Reptil._cantidadR += 1
        
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, color):
        self._colorEscamas = color
    
    def getLargoCola(self):
        return self._largoCola
    
    def setLargoCola(self, largo):
        self._largoCola = largo
        
    def movimiento(self) -> str:
        return "reptar"
    
    @classmethod
    def cantidadReptiles(cls) -> int:
        return cls._cantidadR
    
    @classmethod
    def getListado(cls):
        return cls._listado
    
    @classmethod
    def crearIguana(cls,nombre = "", edad = 0, genero = ""):
        cls.iguanas += 1
        iguana = Reptil(nombre,edad,"humedal",genero,"verde",3)
        return iguana
    
    @classmethod
    def crearSerpiente(cls,nombre = "", edad = 0, genero = ""):
        cls.serpientes += 1
        serpiente = Reptil(nombre,edad,"jungla",genero,"blanco",1)