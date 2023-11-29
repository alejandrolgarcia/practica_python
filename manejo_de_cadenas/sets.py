mi_set = set((1, 2, 3, 4, 5))
print(type(mi_set))
print(mi_set)

otro_set = {6, 7, 8, 9}
print(type(otro_set))
print(otro_set)

# buscar un elemento en un set
print(1 in mi_set)

# union de sets
s1 = {1, 2, 3, 4}
s2 = {4, 4, 6, 7}
s3 = s1.union(s2)
print(s3)

# metodo agregar
s1.add(7)
print(s1)

# metodo para remover
s1.remove(1)
print(s1)

# el metodo discard no regresa error si un elemento no existe en el set
s1.discard(9)
print(s1)

# el metodo pop toma un elemento aleatorio y lo elimina
val = s1.pop()
print(val)

# limpiar el set
s1.clear()
print(s1)