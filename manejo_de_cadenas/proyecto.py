# La consigna es la siguiente: vas a crear un programa que primero le pida al usuario que
# ingrese un texto. Puede ser un texto cualquiera: un artículo entero, un párrafo, una frase, un
# poema, lo que quiera. Luego, el programa le va a pedir al usuario que también ingrese tres
# letras a su elección y a partir de ese momento nuestro código va a procesar esa información
# para hacer cinco tipos de análisis y devolverle al usuario la siguiente información:

# solicitud de informacion al usuario
frase = input('Ingresa tu frase favorita: ')
letra1 = input('Ingresa la primer letra de tu elección: ')
letra2 = input('Ingresa la segunda letra de tu elección: ')
letra3 = input('Ingresa la tercera letra de tu elección: ')

# contar las veces que aparece cada caracter en el texto
frase_min = frase.lower()
dic = {
    letra1: frase_min.count(letra1),
    letra2: frase_min.count(letra2),
    letra3: frase_min.count(letra3),
}

print('Los caracteres elejidos aparecen las siguientes veces en el texto:')
print(dic)

# conteo de palabras del texto
conteo_palabras = frase.split()
print(f'El texto ingresado tiene {len(conteo_palabras)} palabras')

# primera y ultima letra del texto
print(f'Primer letra: {frase[0]}')
print(f'Ultima letra: {frase[-1]}')

# frase invertida
frase_invertida = conteo_palabras[::-1]
nueva_frase = " ".join(frase_invertida)
print(f'Frase envertida: {nueva_frase}')

# encontrar si la palabra python existe en el texto
existe = 'Python' in frase
print(existe)
