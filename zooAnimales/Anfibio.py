from zooAnimales.Animal import Animal

class Anfibio(Animal):
    _listado = []
    _cantidadAnf = 0
    ranas = 0
    salamandras = 0
    
    def __init__(self,nombre = "", edad = 0, habitat = "", genero = "", colorPiel = "", venenoso=False):
        super().__init__(nombre,edad,habitat,genero)
        Anfibio._listado.append(self)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._cantidadAnf += 1
    
    
    
    def isVenenoso(self):
        return self._venenoso
    
    def setVenenoso(self, venenoso):
        self._venenoso = venenoso
        
    def getColorPiel(self):
        return self._colorPiel
    
    def setColorPiel(self, color):
        self._colorPiel = color
    
    def movimiento(self) -> str:
        return "saltar"
    
    @classmethod
    def cantidadAnfibios(cls) -> int:
        return cls._cantidadAnf
    
    @classmethod
    def getListado(cls):
        return cls._listado
    
    @classmethod
    def crearRana(cls,nombre = "", edad = 0, genero = ""):
        cls.ranas += 1
        rana = Anfibio(nombre,edad,"selva",genero,"rojo",True)
        return rana
    
    @classmethod
    def crearSalamandra(cls,nombre = "", edad = 0, genero = ""):
        cls.salamandras += 1
        salamandra = Anfibio(nombre,edad,"selva",genero,"negro y amarillo",False)
        return salamandra