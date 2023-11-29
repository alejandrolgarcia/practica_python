mi_lista = ['A', 'B', 'C', 'D', 'E']
mi_lista2 = ['W', 'X', 'Y', 'Z']
mi_lista3 = [3, 5, 1, 0, 7, 2]

# podemos determinar el tamaño de la lista
print(len(mi_lista))
# tambien se puede acceder a un elemento particular
print(mi_lista[3])
print(mi_lista[0:3])

# concatenacion de listas
print(mi_lista + mi_lista2)

# las listas son mutables
nueva_lista = mi_lista + mi_lista2
nueva_lista[2] = 'ALFA'

# agregar un nuevo elemento a la lista
nueva_lista.append('BETA')
print(nueva_lista)

# con pop se puede eliminar el ultimo elemento o indicar la posicion
print(nueva_lista.pop(2))

# ordenar la lista
mi_lista3.sort()
print(mi_lista3)

# ordenar del mayor a menor
nueva_lista.reverse()
print(nueva_lista)
