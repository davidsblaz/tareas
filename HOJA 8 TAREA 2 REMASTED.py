numero = int(input("Ingrese un número: ")) 
suma = 0
n = 1

while n <= numero:  
    suma += n  
    print(f"La suma hasta {n} es: {suma}") 
    n += 1  

print(f"La suma total es: {suma}")  