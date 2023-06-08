import time  # Importa el módulo 'time' que proporciona funciones relacionadas con el tiempo

import random  # Importa el módulo 'random' que proporciona funciones para generar números aleatorios

# Funciones

def generar_primo():
    # Genera un número primo grande aleatorio
    while True:
        primo = random.randint(2**10, 2**11)
        if es_primo(primo):
            return primo

def es_primo(num):
    # Verifica si un número es primo
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generar_claves():
    # Genera las claves pública y privada
    p = generar_primo()  # Número primo grande
    g = random.randint(2, p - 1)  # Generador aleatorio
    a = random.randint(2, p - 2)  # Clave privada, se elige para evitar los valores extremos 1 y p - 1,
    h = pow(g, a, p)  # Clave pública
    return p, g, h, a

def cifrar(mensaje, p, g, h):
    mensaje_cifrado = []  # Lista para almacenar el mensaje cifrado
    k = random.randint(1, p - 2)  # Número aleatorio secreto

    for letra in mensaje:
        # Cálculo del cifrado para cada letra del mensaje
        r = pow(g, k, p)  # Cálculo de r
        s = (letra * pow(h, k, p)) % p  # Cálculo de s

        cifrado_letra = (r, s)  # Tupla con los valores cifrados de la letra
        mensaje_cifrado.append(cifrado_letra)  # Agregar tupla cifrada a la lista

    return mensaje_cifrado  # Devolver mensaje cifrado como lista de tuplas

def descifrar(mensaje_cifrado, p, x):
    mensaje_descifrado = ''  # Cadena de texto para almacenar el mensaje descifrado

    for letra_cifrada in mensaje_cifrado:
        r = letra_cifrada[0]  # Obtener el valor r de la tupla cifrada
        s = letra_cifrada[1]  # Obtener el valor s de la tupla cifrada

        inverso = pow(r, p - 1 - x, p)  # Cálculo del inverso de r
        letra_descifrada = (s * inverso) % p  # Cálculo de la letra descifrada

        mensaje_descifrado += chr(letra_descifrada)  # Agregar letra descifrada a la cadena

    return mensaje_descifrado  # Devolver mensaje descifrado como cadena de texto

# Partes principales del programa

inicio_lectura = time.time()
# El archivo.txt debe estar en el mismo directorio
with open('texto10.txt', 'r') as archivo:
    # Etapa 1: Leer el archivo de texto
    texto = archivo.read()
tiempo_lectura = (time.time() - inicio_lectura) * 1000  # Convertir a milisegundos

inicio_generacion_claves = time.time()
# Etapa 2: Generar claves de cifrado
p_emisor, g_emisor, h_emisor, a_emisor = generar_claves()
p_receptor, g_receptor, h_receptor, a_receptor = generar_claves()
tiempo_generacion_claves = (time.time() - inicio_generacion_claves) * 1000  # Convertir a milisegundos

inicio_cifrado = time.time()
# Etapa 3: Cifrar el texto
mensaje_cifrado = cifrar([ord(letra) for letra in texto], p_receptor, g_receptor, h_receptor)
tiempo_cifrado = (time.time() - inicio_cifrado) * 1000  # Convertir a milisegundos

inicio_descifrado = time.time()
# Etapa 4: Descifrar el texto cifrado
mensaje_descifrado = descifrar(mensaje_cifrado, p_receptor, a_receptor)
tiempo_descifrado = (time.time() - inicio_descifrado) * 1000  # Convertir a milisegundos

# Impresión de resultados
print("----------------------------------------------------------------------------------------------Cifrado asimetrico ELGAMAL----------------------------------------------------------------------------------------------")
print("Texto original:")
print("\033[32m" + texto + "\033[0m")
print("Tiempo de lectura:", tiempo_lectura, "milisegundos")
print("")

print("Clave pública del emisor:")
print("\033[32m" + "p: " + str(p_emisor) + "\033[0m")
print("\033[32m" + "g: " + str(g_emisor) + "\033[0m")
print("\033[32m" + "h: " + str(h_emisor) + "\033[0m")
print("")

print("Clave privada del emisor:")
print("\033[32m" + "a: " + str(a_emisor) + "\033[0m")
print("")

print("Clave pública del receptor:")
print("\033[32m" + "p: " + str(p_receptor) + "\033[0m")
print("\033[32m" + "g: " + str(g_receptor) + "\033[0m")
print("\033[32m" + "h: " + str(h_receptor) + "\033[0m")
print("")

print("Clave privada del receptor:")
print("\033[32m" + "a: " + str(a_receptor) + "\033[0m")
print("")

print("Tiempo de generación de claves:", tiempo_generacion_claves, "milisegundos")
print("")

print("Texto cifrado:")
print("\033[32m" + str(mensaje_cifrado) + "\033[0m")
print("Tiempo de cifrado:", tiempo_cifrado, "milisegundos")
print("")

print("Texto descifrado:")
print("\033[32m" + str(mensaje_descifrado) + "\033[0m")

print("Tiempo de descifrado:", tiempo_descifrado, "milisegundos")

print("----------------------------------------------------------------------------------------------Resumen de tiempos en las etapas----------------------------------------------------------------------------------------------")
print("")
print("Tiempo de lectura:", tiempo_lectura, "milisegundos")
print("")
print("Tiempo de generación de claves:", tiempo_generacion_claves, "milisegundos")
print("")
print("Tiempo de cifrado:", tiempo_cifrado, "milisegundos")
print("")
print("Tiempo de descifrado:", tiempo_descifrado, "milisegundos")