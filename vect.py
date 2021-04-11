for valor in range(10):
    print(valor)

for valor in range(1, 11):
    print(valor)

for valor in range(2, 100, 2):
    print(valor)
print("Hola")

for i in range(1, 11):
    for j in range(1, 6):
        print(i, j)

# ciclo while

while True:
    print("Hola")
    break

# i = i+2
i = 2
while i <= 10:
    print(i)
i += 2

# HUA que imprima el ganador de una elección de 2 candidatos
cant_uno = 0
cant_dos = 0
num_votos = int(input('Digite la cantidad de personas a votar: '))
for n in range(1, num_votos+1):
    while True:
        voto = int(input(f'Digite el voto {n} Candidato uno[1] o dos[2]'))
        
        
# HUA que de las notas de un estudiante y el promedio

notas = 0
n_notas = int(input('Digite el número de notas del estudiante: '))
for i in range(1, n_notas + 1):
    while True:
        nota = float(input(f'Digite la nota número {i}: '))
        if nota < 5 and nota > 0: break
    notas = notas + nota
prom = notas / n_notas
prom = round(prom, 2)
print(f'El promedio académico de las {n_notas} notas es de: {prom}')

# HUA que imprima el ganador de una elección de dos candidatos

# Tipos de colecciones

# Listas o vectores
# Tipo de dato mutable y ordenado

a = [2, 3, 4]
b = [2, True, 'hola', 3.4]
c = [2[True, False], ['hola', 'mundo'], [2.3, 3.4, 4.6, 7.8]]

for valor in a:
    print(valor)

for valor in b:
    print(valor)

for valor in c:
    print(valor)

a[0] = 7
print(b[2])

a = [2, 3, 4]
a.append(5)  # Agrega el elemento al final de la lista
a.remove(3)  # Elimina de la lista un elemento del valor
a.pop()  # Elimina el último elemento del vector
a.pop(1)  # Elimina un elemento por posición
a.clear()  # Elimina todos los elementos del vector
# del a
4 in a  # Busca el elemento 4 dentro de a
len(a)  # Cantidad de elementos de la lista
b = a  # asignación de b en el mismo espacio de memoria que a
id(a)  # Convierte en decimal la dirección en memoria de un objeto
b = a[:]  # Copia de los elementos de a
c = b[0:3]
c = b[:3]
c = b[2:]

# Tuplas
# Tipo de dato inmutable y ordenado

a = (1, 2, 3, 4)
print(a[1])
a = (1, 'hola', True, 4.5)
a = (1, ['hola', 'Mundo'], True, 4.5)
a = (1, ['hola', 'Mundo'], (True, False), 4.5)
b = a[:2]
4 in a

# Set
# Mutables y NO ordenados

a = {1, 2, 3, 4}
a = {7, 2, 1, 5, 9, 9}

# Diccionario
# Mutable pero no ordenado

a = {'nombre': 'Roberto', 'apellido': 'Morales'}
a = {1: 'Roberto', 2: 'Morales'}

a['nombre']
a['nombre'] = 'Carlos'

for valor in a():
    print(valor)

for valor in a.values():
    print(valor)

for key, valor in a.items():
    print(key, valor)

for valor in a.items():
    print(key, valor)


# Funciones

def nombre_funcion():
    pass


def hola_mundo():
    print('Hola Mundo')


def saludo(nombre='Mundo'):
    print(f'Hola {nombre}')


def saludar():
    print('Hola Mundo')


def saludar3():
    print('Hola Mundo tres')


def saludar_nombre(nombre):
    print(f"Hola {nombre}")


# Parámetros opcionales
def saludarq(nombre="Mundo"):
    print(f"Hola {nombre}")


def saludar4(nombre, apellido=""):
    print(f'Hola {nombre} {apellido}')


# No se puede tener parámetro obligatorio después de uno opcional
def saludar4(nombre="", apellido):
    print('Hola {nombre} {apellido}')


def saludar5(*nombres):
    for nombre in nombres:
        print(nombre)


def saludar6(**nombres):
    print(nombres)


saludar6(nombre='Roberto', nombre2='Carlos')


def saludar7(*nombres, **apellidos):
    print(nombres)
    print(apellidos)


saludar7(nombre='Roberto', 'Cesar', apellido1='Morales', apellido2='Ortega')


def saludar8(nombre, apellido):
    print(f'Hola {nombre} {apellido}')


saludar8(apellido='roberto', nombre='manuel')


def suma(numero_uno, numero_dos):
    suma = numero_uno + numero_dos
    return suma


def suma2(*numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma


def operaciones(numero_uno, numero_dos):
    suma = numero_uno + numero_dos
    resta = numero_uno - numero_dos
    mult = numero_uno * numero_dos
    div = numero_uno / numero_dos
    return suma, resta, mult, div


op = operaciones(3, 4)
suma, resta, mult, div = operaciones(3, 4)
_, _, _, div = operaciones(3, 4)


# HUA que dado los n elementos de un vector, calcule la sumatoria de elementos

numeros = []
n_elementos = int(input('Digite el número de elementos del vector: '))
for i in range(1, n_elementos + 1):
    numero = float(input(f'Digite el elemento número {i}: '))
    numeros.append(numero)
sumatoria = sum(numeros)
print(f'Vector final: {numeros}')
print(f'La sumatoria de los {n_elementos} elementos es: {sumatoria}')
print(f'El elemento de menor valor del vector es: {min(numeros)}')
print(f'El elemento de mayor valor del vector es: {max(numeros)}')


# HUA que dado los n elementos de un vector, calcule la sumatoria de elementos

i = 1
numeros = []
while True:
    numero = float(input(f'Digite el elemento número {i} o digite 0 para salir: '))
    if numero == 0:
        break
    i += 1
    numeros.append(numero)

    sumatoria = sum(numeros)
print(f'Vector final: {numeros}')
print(f'La sumatoria del vector es: {sumatoria}')
print(f'El elemento de menor valor del vector es: {min(numeros)}')
print(f'El elemento de mayor valor del vector es: {max(numeros)}')





































































