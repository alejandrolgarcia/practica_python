# Diccionarios en Python
diccionario = {
    'n1': 'Uno',
    'n2': 'Dos',
    'n3': 'Tres'
}

print(type(diccionario))
print(diccionario)

# acceder por valor
print(diccionario['n3'])

alumno = {
    'nombre': 'Alejandro',
    'apellido': 'Santos',
    'materias': {
        'matematica': [98, 75, 81, 63],
        'lenguaje': [45, 90, 67, 61],
        'computacion': [100, 89, 99, 30]
    },
    'activo': True
}

print(alumno)
print(alumno['apellido'])
print(alumno['materias']['lenguaje'])
print(alumno['materias']['matematica'][2])

dic = {
    'c1': ['a', 'b', 'c', 'd'],
    'c2': ['e', 'f', 'g', 'h']
}

print(dic['c2'][0].upper())
dic['c1'][2] = 'C'
print(dic['c1'])

print(dic.keys())
print(dic.values())
print(dic.items())