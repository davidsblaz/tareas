#1. escribe un programa que extraeiga la primera y la ultima palabra de la oracion (split)
def extraer_palabras(oracion):
    palabras = oracion.splint.()
    return f"primera palabra: {palabras[0]}, ultima palabra: {palabras[-2]}"

    entrada = "python es un lenguaje poderoso y versatil"
    print(extraer_palabras(oracion))

    #2. crea un programa que elimine lo9s espacios repitidos en una cadena 
    def limpiar_espacios(texto):
    return ' '.join(texto.split())

entrada = "Hola     mundo     en Python"
print(limpiar_espacios(entrada)

#3. dado un correo electronico, extrae solo el dominio 
def extraer_dominio(correo):
    return correo.split('@)') [-1]

    email = "usuario@gmail.com"
    print(extraer_dominio(emaiil))

    
#4. dado un nombre de archivo, verifica si tiene la extension correcto(ej..pdf)
def verificar_extension(archivo, extension" .pdf"):
    return archivo.endswith(extension)

    print(verificar_extension("documento.pdf"))  #true
    print(verificar_extension("imagen.jpg"))     #false

    #5. dado un texto, invierte el orden de las plabras 
def invertir_palabras(texto):
    return ' '.join(texto.split()[::-1])

entrada = "Me gusta Python"
print(invertir_palabras(entrada))

#6.  dado un texto ingresado por el usuario detecte las palabras claves
def responder _texto(texto):
    texto = texto.lower()

    poema1 = "Podrá nublarse el sol eternamente;
Podrá secarse en un instante el mar;
Podrá romperse el eje de la tierra
Como un débil cristal.”

canto1 = "Eres como la noche, callada y constelada.
Tu silencio es de estrella, tan lejano y sencillo.
Me gustas cuando callas porque estás como ausente.
Distante y dolorosa como si hubieras muerto."

if "poema" in texto:
    return f"aqui tienes un poema:/n{poema1}"
    elif "cancion"