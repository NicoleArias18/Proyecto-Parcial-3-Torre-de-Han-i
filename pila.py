# Empezamos con una torre vacia
def crear_pila():
    return []   

def is_empty(pila):
    return len(pila) == 0

# Colocamos un disco en la parte de arriba de la torre y luego Saca el disco que esta hasta arriba, si la torre no esta vacia

def push(pila,disco):
    pila.append(disco)

def pop(pila):
    if is_empty(pila):
        return None
    return pila.pop()


#Consulta de que disco esta arriba sin sacarlo
def peek(pila):
    if is_empty(pila):
        return None
    return pila[-1]

#Cuenta cuantos discos tiene la torre en ese momento
def size(pila):
    return len(pila)



#BLOQUE DE PRUEBA 

if __name__ == "__main__":
    torre_prueba = crear_pila()
    push(torre_prueba, 3)
    push(torre_prueba, 2)
    push(torre_prueba, 1)

    print("Torre inicial:", torre_prueba)
    print("Disco en la cima", peek(torre_prueba))
    print("sacando disco:", pop(torre_prueba))
    print("Torre actual:", torre_prueba)
    print("Cantidad de discos:", size(torre_prueba))
