
# all: una funcion recursiva es una funcion que se llama asi misma

def fact (x):
    if x == 1 :   #! caso base (evita que se vuelva una funcion infinita)
        return 1
    else:
        return x * fact(x-1) #! caso recursivo (llama la misma funcion para hacer mas simple el proceso)


print(fact ( 5 ))