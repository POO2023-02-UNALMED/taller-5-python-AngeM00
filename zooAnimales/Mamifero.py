from zooAnimales.animal import Animal

class Mamifero(Animal):
    _listado = []
    _cantidadM = 0
    caballos = 0
    leones = 0
    
    def __init__(self,nombre = "", edad = 0, habitat = "", genero = "", pelaje = False, patas=0):
        super().__init__(nombre,edad,habitat,genero)
        Mamifero._listado.append(self)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._cantidadM += 1
        
    def isPelaje(self):
        return self._pelaje
    
    def setPelaje(self, pelaje:bool):
        self._pelaje = pelaje
    
    def getPatas(self):
        return self._patas
    
    def setPatas(self, patas:int):
        self._patas = patas
        
    @classmethod
    def cantidadMamiferos(cls) -> int:
        return cls._cantidadM
    
    @classmethod
    def getListado(cls):
        return cls._listado

    @classmethod
    def crearCaballo(cls,nombre = "", edad = 0, genero = ""):
        cls.caballos += 1
        caballo = Mamifero(nombre,edad,"pradera",genero,True,4)
        return caballo
    
    @classmethod
    def crearLeon(cls,nombre = "", edad = 0, genero = ""):
        cls.leones += 1
        leon = Mamifero(nombre,edad,"selva",genero,True,4)
    
    
    