tamaño = int(input("Ingrese cuántos números quiere: "))
base = int(input("Ingrese el número base: "))

arreglo = []

for i in range(1, tamaño + 1):
    arreglo.append(base * i)

print("Múltiplos:", arreglo)