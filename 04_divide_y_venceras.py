
#all : divide y venceras este algoritmo es dificil de implementar pero lo podemos ver en muchas casos de aritmetica basica , ya que al integrarse con recursion podemos tener una herramienta poderosa para resolver cualquier problema aritmetico


#! algoritmo de euclides

def mcd(a, b):
    #! Mostrar los valores actuales
    print(f"Llamada: mcd({a}, {b})")

    #! Caso base: si b es 0, el MCD es a
    if b == 0:
        print(f"b es 0, retorno {a} como MCD")
        return a
    else:
        #! Llamada recursiva con (b, a % b)
        return mcd(b, a % b)







#! ejemplo de sumar varios numeros con divide y venceras y recursividad 

def suma(array):
    if len(array) == 0:
        return 0  # caso base
    else:
        return array[0] + suma(array[1:])  # llamada recursiva

mcd(252, 105)


print(suma ([1,2,3,4]))