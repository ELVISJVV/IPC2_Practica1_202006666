from Nodo import Nodo

class ListaDoble:

    def __init__(self):

        self.primero = None
        self.ultimo = None
        self.size = 0

    #insertar en lista
    def insertar(self, dato):

        nuevo = Nodo(dato)

        if self.primero is None: 

            self.primero = nuevo
            self.ultimo = self.primero
        else: 
            # insertar ultimo
            nuevo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo 
        
            # insertar al principio
            # nuevo.siguiente = self.primero
            # self.primero.anterior = nuevo
            # self.primero = nuevo
        self.size += 1 
    
    #mostrar datos en consola
    def mostrar(self):

        temp = self.primero 

        while temp != None:

            print(temp.getDato().getNombreCliente()) 
            print(temp.getDato().getTiempo()) 
            print(temp.getDato().getTiempoTotal()) 

            temp = temp.siguiente 
    

    
    def mostrarIngredientes(self):
        
        temp = self.primero 

        while temp != None:

            print('F: {}\nC: {}\n'.format(
                temp.dato.tipoIngrediente, temp.dato.tiempoIngrediente))

            temp = temp.siguiente

    
    def returnElement(self, posicion):
        
        actual = self.primero
        i = 1
        
        while actual != None:
            
            if posicion == i:
                
                return actual
                # return actual.dato.nombre
            
            actual = actual.getSiguiente()
            i += 1



    def borrarNodo(self, dato):
        #creamos un nodo temporal
        # nodoTemporal = Nodo("")

        #el temporal empieza en la cabeza
        nodoTemporal = self.primero

        #Mientras que el temporal no sea nulo
        while nodoTemporal != None:

            #validamos si ese nodo es el que busco
            if nodoTemporal.dato == dato:

                #Si ese nodo es la cabeza
                if nodoTemporal == self.primero:
                    
                    # print("Borrando dato en la cabeza")
                    if self.size == 1:
                        self.primero=None
                        self.ultimo=None
                        
                    else:    
                        self.primero = self.primero.siguiente
                        nodoTemporal.siguiente = None
                        self.primero.anterior = None
                #Si ese nodo es la ultimo
                elif nodoTemporal == self.ultimo:
                    # print("Borrando dato en la ultimo")
                    self.ultimo = self.ultimo.anterior
                    nodoTemporal.anterior = None
                    self.ultimo.siguiente = None
                #Si no es ni la ultimo ni la cabeza
                else:
                    # print("Borrando dato del medio")
                    nodoTemporal.anterior.siguiente = nodoTemporal.siguiente
                    nodoTemporal.siguiente.anterior = nodoTemporal.anterior
                    nodoTemporal.siguiente = nodoTemporal.anterior = None
                self.size -= 1
            nodoTemporal = nodoTemporal.siguiente

    def __setitem__(self, indice, dato):
        if indice >= 0 and indice <= self.size:
            actual = self.primero

            for _ in range(indice - 1):
                actual = actual.siguiente

            actual.dato = dato
        else:
            raise Exception('Índice no válido. Está por fuera del rango.')
