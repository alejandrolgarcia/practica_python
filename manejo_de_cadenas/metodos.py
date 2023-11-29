# Metodos comunes para manipular strings

texto = "El objeto String se utiliza para representar y manipular una secuencia de caracteres."

# print(texto.__len__())

# Convertir a mayusculas
print(texto.upper())
print(texto[3:9].upper())

# Convertir a minusculas
print(texto.lower())

# Separar las palabras en un array
# Si le pasamos un parametro, este sera el indicativo para la separacion
print(texto.split())
print(texto.split("t"))

# Unir palabras con .join
a = "Aprender"
b = "python"
c = "es"
d = "genial"
e = " ".join([a, b, c, d])
print(e)

# Buscar un caractero o conjunto de caracteres y devuelve el indice donde se encuentra
# y -1 si no se encuentra el caracter o conjunto de caracteres.
print(texto.find("S"))          # 10 el caracter empieza en la posicion 10
print(texto.find("para"))       # 28 la palabra empieza en la posicion 28
print(texto.find("x"))          # -1 el caracter no se encuentra dentro del string.

# reemplazar caracteres. El primer parametro es a reemplazar y el segundo es el nuevo caracter.
print(texto.replace("a", "x"))
print(texto.replace("para", "xxxx"))
