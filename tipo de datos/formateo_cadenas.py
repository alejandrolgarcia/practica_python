years = 31
months = 8

# con concatenacion
print("Yo tengo " + str(years) + " años y " + str(months) + " meses de edad.")

# con el metodo .format
print("Yo tengo {} años y {} meses de edad.".format(years, months))

# operaciones dentro de .format
print("La suma de {} y {} es {}.".format(years, months, years + months))

# cadenas literales
color = "rojo"
matricula = 458921

print(f"El color del carro es {color} y su matricula es {matricula}.")

