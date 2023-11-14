# conversion implicita

num1 = 20
num2 = 30.5

# Python convierte num1 a float
num1 = num1 + num2

print(type(num1))
print(type(num2))

# conversion de tipos de datos

nota1 = 7.3
print(nota1)
print(type(nota1))

nota2 = int(nota1)
print(nota2)
print(type(nota2))

edad = input("Ingresa tu edad: ")
edad = int(edad)
nueva_edad = edad + 1
print(nueva_edad)