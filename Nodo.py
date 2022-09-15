

class Nodo:

    def __init__(self, dato):

        self.dato = dato
        self.siguiente = None
        self.anterior = None

    # Funciones get
    
    def getDato(self):
        
        return  self.dato
    
    def getSiguiente(self):
        
        return  self.siguiente
    
    def getAnterior(self):
        
        return  self.anterior
    
    # Metodos set
    
    def setDato(self, dato):
        
        self.dato = dato
        
    def setSiguiente(self, siguiente):
        
        self.siguiente = siguiente
        
    def setAnterior(self, anterior):
        
        self.anterior = anterior  
    

