class Animal:
    _totalAnimales = 0
    def __init__(self, nombre = "", edad = 0, habitat = "", genero = ""):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = []
    
    def movimiento(self) -> str :
        return "desplazamiento"
    
    #Getters y setters
    def getNombre(self) -> str:
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre
        
    def getEdad(self) -> int:
        return self._edad
    
    def setEdad(self, edad):
        self._edad = edad
    
    def getHabitat(self) -> str:
        return self._habitat
    
    def setHabitat(self, habitat):
        self._habitat = habitat
    
    def getGenero(self) -> str:
        return self._genero
    
    def setGenero(self, genero):
        self._genero = genero
        
    def getZona(self):
        return self._zona
    
    def setZona(self, zona):
        self._zona.append(zona)
    
    @classmethod
    def totalPorTipo(cls) -> str:
        #imports
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.ave import Ave
        from zooAnimales.reptil import Reptil
        from zooAnimales.pez import Pez
        from zooAnimales.anfibio import Anfibio
        
        cantidadMamiferos = Mamifero.cantidadMamiferos()
        cantidadAves = Ave.cantidadAves()
        cantidadReptiles = Reptil.cantidadReptiles()
        cantidadPez = Pez.cantidadPeces()
        cantidadAnfibios = Anfibio.cantidadAnfibios()
        
        return f'''Mamiferos: {cantidadMamiferos}\nAves: {cantidadAves}\nReptiles: {cantidadReptiles}\nPeces: {cantidadPez}\nAnfibios: {cantidadAnfibios}'''
    
    def __str__(self) -> str:
        frase = ""
        if len(self._zona) != 0:
            nombre = self._zona.__getitem__(0).getNombre()
            frase = f", la zona en la que me ubico es {nombre}, en el {self._zona[0].getZoo().getNombre()}"
        return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"+frase
    
    def toString(self):
        frase = ""
        if len(self._zona) != 0:
            nombre = self._zona.__getitem__(0).getNombre()
            frase = f", la zona en la que me ubico es {nombre}, en el {self._zona[0].getZoo().getNombre()}"
        return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"+frase