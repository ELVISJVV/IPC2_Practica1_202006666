class Orden:
    def __init__ (self, nombreCliente,ingrediente,tiempo,tiempoTotal,cantidadShucos):
        self.nombreCliente = nombreCliente
        self.ingrediente = ingrediente
        self.tiempo = tiempo
        self.tiempoTotal = tiempoTotal
        self.cantidadShucos = cantidadShucos

    def getCantidadShucos(self):
        return self.cantidadShucos

    def getNombreCliente(self):
        return self.nombreCliente

    def getIngrediente(self):
        return self.ingrediente
    def getTiempo(self):
        return self.tiempo
    def getTiempoTotal(self):
        return self.tiempoTotal


    def setTiempoTotal(self, tiempoTotal):
        self.tiempoTotal = tiempoTotal

class Ingredientes:
    def __init__(self, tipoIngrediente, tiempoIngrediente):
        self.tipoIngrediente =tipoIngrediente
        self.tiempoIngrediente = tiempoIngrediente

    def getTipoIngrediente(self):
        return self.tipoIngrediente
    def getTiempoIngrediente(self):
        return self.tiempoIngrediente