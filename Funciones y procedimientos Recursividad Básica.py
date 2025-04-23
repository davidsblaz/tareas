#Ejercicio 1:Crea un procedimiento: es_par_o_impar(n) 
def es_par_o_impar(n):
    if n% 2 == 0:
        print(f"{n} es par")
    else:
        print(f"{n} es impar")

#Ejercicio 2:Crea una función suma_lista
def suma_lista(lista):
    return sum(lista)
#ejmp
#print(suma_lista([1, 2, 3])) >6

#Ejercicio 3:crea una funcion recursiva cuenta regresiva (n)
def cuenta_regresiva(n):
    if n < 0:
        print("¡Despegue!")
    else:
        print(n)
        cuenta_regresiva(n - 1)
#cuenta regresiva 3

#Ejercicio 4:Crear una función recursiva que imprima los números del 1 hasta n
def cuenta_ascendente(n, actual=1):
    if actual <= n:
        print(actual)
        cuenta_ascendente(n, actual + 1)

# Ejemplo:
# cuenta_ascendente(4)

#Ejercicio 5
def suma_hasta(n):
    if n == 1:
        return 1 
    else:
        return n + suma_hasta(n - 1)
#print(suma_hasta(4) ) >10

#Ejercicio 6: Crear una función factorial(n) recursiva
def factoria(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factoria(n - 1)
#factorial(5) → 120

#Ejercicio 7: Mínimo en lista (sin min())
def minimo(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        menor_del_resto = minimo(lista[1:])
        return lista[0] if lista[0] < menor_del_resto else menor_del_resto