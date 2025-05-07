# matriz=[]

# for i in range(3):#la cantidad de filas es 3
#     fila=[]
#     for j in range(3):#la cantida de columnas
#         datos=int(input(f"Ingrese los valores a la matriz [{i}][{j}]:"))
#         fila.append(datos)
#     matriz.append(fila)

# print(matriz)

matriz = []

for i in range(3):  
    fila = []
    for j in range(3): 
        datos = int(input(f"Ingrese los valores a la matriz [{i}][{j}]:"))
        fila.append(datos)
    matriz.append(fila)

print(matriz)

suma = 0
mayores_5 = 0

for fila in matriz:
    for elemento in fila:
        suma += elemento
        if elemento > 5:
            mayores_5 += 1

print(f"Suma total de los elementos: {suma}")
print(f"Cantidad de elementos mayores a 5: {mayores_5}")



#Ejercicio 2
A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

suma = []

for i in range(2):
    fila = []
    for j in range(2):
        fila.append(A[i][j] + B[i][j])
    suma.append(fila)

for fila in suma:
    print(fila)
    


# Ejercicio 3:
# Declara una matriz de 2x3. Pide al usuario un escalar y muestra la matriz multiplicada por ese escalar.

# Definimos la matriz de 2x3
matriz = []

for i in range(2):  
    fila = []
    for j in range(3):  
        valor = int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)


print("\nMatriz original:")
for fila in matriz:
    print(fila)


escalar = int(input("\nIngrese un escalar para multiplicar la matriz: "))


matriz_escalar = []
for fila in matriz:
    nueva_fila = [elemento * escalar for elemento in fila]
    matriz_escalar.append(nueva_fila)

print("\nMatriz multiplicada por el escalar:")
for fila in matriz_escalar:
    print(fila)

# Ejercicio 4:
# Pide al usuario una matriz cuadrada (3x3) y muestra su transpuesta.

# Ingreso de datos para matriz 3x3
matriz = []

for i in range(3):
    fila = []
    for j in range(3):
        valor = int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)


print("\nMatriz original:")
for fila in matriz:
    print(fila)


transpuesta = []

for i in range(3):
    fila_transpuesta = []
    for j in range(3):
        fila_transpuesta.append(matriz[j][i])
    transpuesta.append(fila_transpuesta)


print("\nMatriz transpuesta:")
for fila in transpuesta:
    print(fila)

# Ejercicio 5 (Reto):
# Multiplicación de dos matrices (A x B)

# Definir matrices A (2x3) y B (3x2)
print("Ingrese los valores de la matriz A (2x3):")
A = []
for i in range(2):
    fila = []
    for j in range(3):
        valor = int(input(f"A[{i}][{j}]: "))
        fila.append(valor)
    A.append(fila)

print("\nIngrese los valores de la matriz B (3x2):")
B = []
for i in range(3):
    fila = []
    for j in range(2):
        valor = int(input(f"B[{i}][{j}]: "))
        fila.append(valor)
    B.append(fila)


resultado = []

for i in range(2):
    fila_resultado = []
    for j in range(2):
        suma = 0
        for k in range(3):
            suma += A[i][k] * B[k][j]
        fila_resultado.append(suma)
    resultado.append(fila_resultado)


print("\nResultado de la multiplicación A x B:")
for fila in resultado:
    print(fila)