
def encuentraMenor(array):
    menor = array[0] #! indica el valor menor
    indice_menor = 0 #! indica el indice del valor menor 
    for i in range (1, len (array)):
        if array[i] < menor:
            menor = array[i]
            indice_menor = i
    return indice_menor 
    

def ordenacion_por_seleccion(array): #! ordena un array
    nuevoarr = []
    for i in range(len(array)):
        menor = encuentraMenor(array) #! encuentra el menor elemento en el array y lo añade al nuevo array
        nuevoarr.append(array.pop(menor))

    return nuevoarr

print(ordenacion_por_seleccion([5,3,6,2,10]))
