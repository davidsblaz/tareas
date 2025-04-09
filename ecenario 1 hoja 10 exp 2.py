n = int(input("Ingrese la cantidad de clientes: "))
evaluaciones = []

i = 0
while i < n:
    valor = int(input(f"Cliente {i+1} (1-5): "))
    if 1 <= valor <= 5:
        evaluaciones.append(valor)
        i += 1
    else:
        print("Valor inválido. Ingrese un número entre 1 y 5.")

excelente = 0
muy_buena = 0
buena = 0
regular = 0
malo = 0

j = 0
while j < n:
    if evaluaciones[j] == 5:
        excelente += 1
    elif evaluaciones[j] == 4:
        muy_buena += 1
    elif evaluaciones[j] == 3:
        buena += 1
    elif evaluaciones[j] == 2:
        regular += 1
    elif evaluaciones[j] == 1:
        malo += 1
    j += 1

frecuencias = [0, 0, 0, 0, 0, 0]

k = 0
while k < n:
    valor = evaluaciones[k]
    frecuencias[valor] += 1
    k += 1

respuesta_frecuente = 1
r = 2
while r <= 5:
    if frecuencias[r] > frecuencias[respuesta_frecuente]:
        respuesta_frecuente = r
    r += 1

suma = 0
l = 0
while l < n:
    suma += evaluaciones[l]
    l += 1

promedio = suma / n

clientes_menores = []
m = 0
while m < n:
    if evaluaciones[m] < promedio:
        clientes_menores.append(m + 1)
    m += 1

porcentaje_menor = (len(clientes_menores) / n) * 100

print(f"\nRespuestas:\na) Excelente: {excelente}\n   Muy Buena: {muy_buena}\n   Buena: {buena}\n   Regular: {regular}\n   Malo: {malo}")
print(f"\nb) Respuesta más frecuente: {respuesta_frecuente}")
print(f"c) Promedio: {promedio:.2f}")
print(f"   Clientes con respuesta menor al promedio: {clientes_menores}")
print(f"   Porcentaje menor al promedio: {porcentaje_menor:.2f}%")