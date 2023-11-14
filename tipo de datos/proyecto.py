# Proyecto unidad tipo de datos
name = input("Cuál es tu nombre: ")
sales = float(input(f"Cuántas ventas tuviste en el mes {name}? "))

commission = (sales * 13) / 100

print(f"Hola {name}, tu comision por ventas este mes es {round(commission, 2)}.")