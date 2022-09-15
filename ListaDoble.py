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


    def obtenerPaciente(self, nombre):

        temp = self.primero

        while temp != None:

            if nombre.lower() == temp.dato.nombre.lower(): #cuando encuentre el elemento deseado retornara el dato que contiene el nodo
                return temp.dato # se retorna el dato
            
            temp = temp.siguiente #el temp recorre la lista
        
        if temp == None: #en el caso que no se haya encontrado el paciente.

            print('Paciente no encontrado.') 

    #obtener un elemento por la posición en la lista
    def obtenerElemento(self, posicion):

        i = 1 #nuestra lista comienza en la posición 1
        temp = self.primero

        while temp != None:

            if i == posicion:
                # print(temp.dato)
                return temp.dato

            i += 1
            temp = temp.siguiente
        
        if temp == None:

            print('Elemento no encontrado.')
    
    def verPacientes(self):
        
        actual = self.primero
        i = 1
        print('|------------------- Pacientes -------------------|')
        print()
        
        while actual != None:
            
            print('→ '+ str(i)+ '. ' + "Paciente: " + str(actual.getDato().getNombre()) + "   Edad: " + str(actual.getDato().getEdad()))
            print()
            
            i += 1 
            actual = actual.getSiguiente()

    def returnElement(self, posicion):
        
        actual = self.primero
        i = 1
        
        while actual != None:
            
            if posicion == i:
                
                return actual
                # return actual.dato.nombre
            
            actual = actual.getSiguiente()
            i += 1

    def __getitem__(self, indice):
        if indice >= 0 and indice < self.size:
            actual = self.ultimo

            for i in range(indice):
                actual = actual.siguiente

            return actual.getDato()
        else:
            raise Exception('Índice no válido. Está por fuera del rango.')

    def eliminar(self, dato):
        actual = self.primero
        eliminado = False

        if actual is None:
            eliminado = False
        elif actual.dato == dato:
            self.primero = actual.siguiente
            self.primero.anterior = None
            eliminado = True
        elif self.ultimo.dato == dato:
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = None
            eliminado = True
        else:
            while actual:
                if actual.dato == dato:
                    # Antes: 2 = 3 = 5 = 7 = 11
                    # Actual: 3
                    # Después: 2 = 5 = 7 = 11
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                    eliminado = True
                actual = actual.siguiente

        if eliminado:
            self.size -= 1

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
