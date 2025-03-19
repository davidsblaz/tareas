def numero_a_texto(n):
    unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez", 
                "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve"]
    decenas = ["", "", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]

    if n < 20:
        return unidades[n]
    elif n % 10 == 0:
        return decenas[n // 10]
    else:
        return f"{decenas[n // 10]} y {unidades[n % 10]}"

print(numero_a_texto(4))
print(numero_a_texto(40))
print(numero_a_texto(99))