
# all : encuntra cualquier elemento mucho mas rapido que una busqueda ordinaria ya que dividide el carga por logica entre valores menores y mayores pero esto solo si conoce la posicion en la que se encuentra el elemento

def busqueda_binaria(lista, elemento):

    #!menor y mayor indican en que parte de la lista se buscara
    menor = 0  
    mayor =len (lista) -1 


    #!minetras no hayas reducido la busqueda a un solo elemento
    while menor <= mayor :
        medio = (menor+mayor)//2 #! comprueba el elemento central
        estimado = lista[medio]
        if estimado == elemento:#!elemeneto encontrado
            return medio
        if estimado > elemento:#! el numero era muy alto
            mayor = medio-1
        else : #! el numero era muy bajo
            menor = medio +1

    return None #!elemento no existe



mi_lista = [1,3,5,7,9] #! probamos la busqueda

print (busqueda_binaria(mi_lista, 7)) #!llama la funcion 