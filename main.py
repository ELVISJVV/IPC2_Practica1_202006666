from tkinter.tix import Tree
from ListaDoble import ListaDoble
from Orden import Ingredientes, Orden
from os import startfile, system


if __name__ == '__main__':

    salir = False
    listaOrdenes = ListaDoble()
    listaIngredientes = ListaDoble()
    tiempoOrden = 0
    # tiempo = 0
    tiempoTotal = 0
#  python main.py

    def generarGraphviz(listaOrdenes):
        graphviz = '''
        digraph L{
        node [shape=box fillcolor="#FFEDBB" style = filled]

        subgraph cluster_p{
            label="Orden de Clientes"
            bgcolor = "#398D9C"
        '''

        size = int(listaOrdenes.size)

        for i in range(1, size+1, 1):
            # print("numero de rango")
            # print(i)
            # print("numero de size")
            # print(size)
            cliente = listaOrdenes.returnElement(int(i))
            # print(cliente)
            nombreCliente = cliente.getDato().getNombreCliente()
            # print(nombreCliente)
            graphviz += 'Columna' + str(i) + '''[label=<<TABLE  BORDER="0" CELLBORDER="1" CELLSPACING="0"> 
            <TR>
            <TD  colspan="2">''' + nombreCliente + '''</TD>
            </TR>

            <TR>

            <TD>Cant. Shucos</TD>
            <TD>''' + str(int(listaOrdenes.returnElement(i).getDato().getCantidadShucos())) + '''</TD>
            </TR>
            <TR>
            <TD>Ingredientes</TD>
            <TD>'''
            ingredients = listaOrdenes.returnElement(int(i))

            todoslosingredientes = ingredients.getDato().getIngrediente()
            # todoslosingredientes.mostrarIngredientes()
            sizeIngredientes = int(todoslosingredientes.size)
            for x in range(1, sizeIngredientes+1, 1):
                graphviz += todoslosingredientes.returnElement(
                    x).getDato().getTipoIngrediente() + '<br/>'

            graphviz += '</TD>'

            graphviz += '''
            </TR >

            <TR>
            <TD>Tiempo Orden</TD>
            <TD>''' + str(listaOrdenes.returnElement(i).getDato().getTiempo()) + ' min'+'''</TD>
            </TR>
            <TR>
            <TD>Tiempo Total</TD>
            <TD>''' + str(listaOrdenes.returnElement(i).getDato().getTiempoTotal()) + ' min' + '''</TD>
            </TR>

            </TABLE>>, fillcolor=yellow]; '''

        graphviz += '''{rank = same;'''

        for a in range(1, size+1, 1):
            if a == size:
                graphviz += 'Columna' + str(a) + '}'
            else:
                graphviz += 'Columna' + str(a) + ';'

        for i in range(size, 0, -1):
            if i-1 == 0:
                break
            graphviz += 'Columna' + str(i) + '-> Columna' + str(i-1) + ';'
       

        graphviz += ''' 
        }
        }
        '''

        miArchivo = open("graphviz.dot", 'w')
        miArchivo.write(graphviz)
        miArchivo.close()

        system('dot -Tpng graphviz.dot -o graphviz.png')
        # system('cd ./graphviz.png')
        startfile('graphviz.png')

    while salir == False:

        print("======= MENU PRINCIPAL ========")
        print("1. Ingresar Orden")
        print("2. Despachar Orden")
        print("3. Datos del Desarrollador")
        print("4. Salir")
        print("================================")
        opcion = input()

        if opcion == '1':

            print(' \nIngrese el nombre del cliente:')
            nombre = input()
            salirNoShucos= False

            while salirNoShucos == False:
                
                print("¿Cuantos shucos deseas?")
                numeroShucos = input()
                # print(numeroShucos.isnumeric() )
                if numeroShucos.isnumeric() == True:
                    if int(numeroShucos) > 0:
                        numeroShucos = float(numeroShucos)
                        salirNoShucos = True   
                    else:
                        print("Ingrese una cantidad valida mayor a cero")
                else:
                    print("Ingrese una cantidad valida")

            print(" \n¿Que ingrediente desea?")

            salirIngre = False

            while salirIngre == False:
                tiempoOrden = 0
                tiempo = 0
                print("======= MENU INGREDIENTES ========")
                print("1. Salchica")
                print("2. Chorizo")
                print("3. Salami")
                print("4. Longaniza")
                print("5. Costilla")
                print("================================")
                opcion2 = input()

                if opcion2 == "1":
                    ingrediente = "Salchica"
                    tiempo = 2
                    tiempoOrden += tiempo
                    ingredientes = Ingredientes(ingrediente, tiempo)
                    listaIngredientes.insertar(ingredientes)
                    salirIngre = True
                elif opcion2 == '2':
                    ingrediente = "Chorizo"
                    tiempo = 3
                    tiempoOrden += tiempo
                    ingredientes = Ingredientes(ingrediente, tiempo)
                    listaIngredientes.insertar(ingredientes)
                    salirIngre = True
                elif opcion2 == '3':
                    ingrediente = "Salami"
                    tiempo = 1.5
                    tiempoOrden += tiempo
                    ingredientes = Ingredientes(ingrediente, tiempo)
                    listaIngredientes.insertar(ingredientes)
                    salirIngre = True
                elif opcion2 == '4':
                    ingrediente = "Longaniza"
                    tiempo = 4
                    tiempoOrden += tiempo
                    ingredientes = Ingredientes(ingrediente, tiempo)
                    listaIngredientes.insertar(ingredientes)
                    salirIngre = True
                elif opcion2 == '5':
                    ingrediente = "Costilla"
                    tiempo = 6
                    tiempoOrden += tiempo
                    ingredientes = Ingredientes(ingrediente, tiempo)
                    listaIngredientes.insertar(ingredientes)
                    salirIngre = True
                else:
                    print("Ingrese una opcion valida")
            
            salirIngre = False

            while salirIngre == False:
                # print(tiempoOrden)
                print("======= ¿Deseas Agregar Mas Ingredientes? ========")
                print("1. Salchica")
                print("2. Chorizo")
                print("3. Salami")
                print("4. Longaniza")
                print("5. Costilla")
                print("6. NO AGREGAR MAS INGREDIENTES")
                print("================================")
                opcion2 = input()
                
                if opcion2 == '6':
                    salirIngre = True
                elif opcion2 == "1":
                    ingrediente = "Salchica"
                    tiempo = 2
                    tiempoOrden += tiempo
                    ingredientes = Ingredientes(ingrediente, tiempo)
                    listaIngredientes.insertar(ingredientes)
                elif opcion2 == '2':
                    ingrediente = "Chorizo"
                    tiempo = 3
                    tiempoOrden += tiempo
                    ingredientes = Ingredientes(ingrediente, tiempo)
                    listaIngredientes.insertar(ingredientes)
                elif opcion2 == '3':
                    ingrediente = "Salami"
                    tiempo = 1.5
                    tiempoOrden += tiempo
                    ingredientes = Ingredientes(ingrediente, tiempo)
                    listaIngredientes.insertar(ingredientes)
                elif opcion2 == '4':
                    ingrediente = "Longaniza"
                    tiempo = 4
                    tiempoOrden += tiempo
                    ingredientes = Ingredientes(ingrediente, tiempo)
                    listaIngredientes.insertar(ingredientes)
                elif opcion2 == '5':
                    ingrediente = "Costilla"
                    tiempo = 6
                    tiempoOrden += tiempo
                    ingredientes = Ingredientes(ingrediente, tiempo)
                    listaIngredientes.insertar(ingredientes)
                else:
                    print("Ingrese una opcion validad")

            tiempoOrden = tiempoOrden*numeroShucos
            tiempoTotal += tiempoOrden

            if listaOrdenes.size == 0:
                orden = Orden(nombre, listaIngredientes, tiempoOrden, tiempoOrden, numeroShucos)
                listaOrdenes.insertar(orden)
            else:
                tiempoTotal=listaOrdenes.returnElement(listaOrdenes.size).getDato().getTiempoTotal() + tiempoOrden

                orden = Orden(nombre, listaIngredientes,tiempoOrden, tiempoTotal, numeroShucos)
                listaOrdenes.insertar(orden)

            listaIngredientes = ListaDoble()
            generarGraphviz(listaOrdenes)
        elif opcion == '2':
            
            nuevoTiempoTotal = 0
            size = int((listaOrdenes.size))
            if size >=2:
                tiempoMenos =listaOrdenes.returnElement(1).getDato().getTiempo()
                listaOrdenes.borrarNodo( listaOrdenes.returnElement(1).getDato())
                size = int((listaOrdenes.size))
                for z in range (1,size+1,1):
                    tiempoResta= float(listaOrdenes.returnElement(z).getDato().getTiempoTotal())
                    nuevoTiempoTotal =tiempoResta - tiempoMenos
                    listaOrdenes.returnElement(z).getDato().setTiempoTotal(nuevoTiempoTotal)
                    
                    

                generarGraphviz(listaOrdenes)
            elif size <=0:
                print("")
                print("NO HAY PEDIDOS POR ENTREGAR")
                print("")

            else: 
                tiempoMenos = listaOrdenes.returnElement(
                    1).getDato().getTiempo()
                listaOrdenes.borrarNodo( listaOrdenes.returnElement(1).getDato())

                size = int((listaOrdenes.size))
                for z in range (1,size+1,1):
                    tiempoResta= float(listaOrdenes.returnElement(z).getDato().getTiempoTotal())
                    nuevoTiempoTotal =tiempoResta - tiempoMenos
                    listaOrdenes.returnElement(z).getDato().setTiempoTotal(nuevoTiempoTotal)
                
                startfile('Completado.png')
                
                print("")
                print("Se han entregado todos los pedidos")
                print("")
         
        elif opcion == '3':
            print('\n')
            print("======= DATOS DEL DESARROLLADOR ========")
            print("")
            print("Nombre. Elvis Joseph Vásquez Villatoro ")
            print("Carné: 202006666")
            print("")
            print("=====================================")
            print('\n')

        elif opcion == '4':
            print("Hasta pronto")
            salir = True
        else:
            print("\n")
            print("Ingrese una opcion valida")
            print("\n")
