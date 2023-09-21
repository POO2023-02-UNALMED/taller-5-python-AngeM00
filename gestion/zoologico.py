class Zoologico:
    def __init__(self, nombre = "",ubicacion="", zonas = None):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = zonas
        
    #Getters y setters
    def getZona(self):
        return self._zonas
    
    def getNombre(self) -> str:
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre
        
    def getUbicacion(self) -> str:
        return self._ubicacion
    
    def setUbicacion(self,ubicacion):
        self._ubicacion = ubicacion
        
    def agregarZonas(self, zona) -> None:
        if self._zonas == None:
            self._zonas = []
            
        self._zonas.append(zona)
        
    def cantidadTotalAnimales(self) -> int:
        cantidad = 0
        for zona in self._zonas:
            cantidad += zona.cantidadAnimales()
        
        return cantidad
    