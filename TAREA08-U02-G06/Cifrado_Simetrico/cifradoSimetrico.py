import time
from cryptography.fernet import Fernet
import colorama
from colorama import Fore, Style

def generar_clave():
    clave = Fernet.generate_key()
    return clave

def cifrar_texto(texto, clave):
    f = Fernet(clave)
    texto_cifrado = f.encrypt(texto.encode())
    return texto_cifrado

def descifrar_texto(texto_cifrado, clave):
    f = Fernet(clave)
    texto_descifrado = f.decrypt(texto_cifrado)
    return texto_descifrado.decode()

def main():

    # Leer archivo con texto a cifrar
    inicio = time.time()
    with open("archivo_10.txt", "r") as archivo:
        texto_original = archivo.read()
    fin = time.time()
    tiempo_lectura = (fin - inicio) * 1000  # Tiempo transcurrido en milisegundos

    # Texto original
    print("\n\033[1mTexto Original:\033[0m")
    print(Fore.GREEN, texto_original)

    # Generar y/o imprimir la(s) clave(s) de cifrado
    inicio = time.time()
    clave = generar_clave()
    fin = time.time()
    tiempo_generar_clave = (fin - inicio) * 1000  # Tiempo transcurrido en milisegundos
    print(Style.RESET_ALL + "\n\033[1mClave generada:\n\033[0m")
    print(Fore.GREEN, clave)
    

    # Cifrar e imprimir el texto cifrado
    inicio = time.time()
    texto_cifrado = cifrar_texto(texto_original, clave)
    fin = time.time()
    tiempo_cifrar = (fin - inicio) * 1000  # Tiempo transcurrido en milisegundos
    print(Style.RESET_ALL + "\n\033[1mTexto cifrado:\n\033[0m")
    print(Fore.GREEN, texto_cifrado)

    # Descifrar e imprimir el texto claro
    inicio = time.time()
    texto_descifrado = descifrar_texto(texto_cifrado, clave)
    fin = time.time()
    tiempo_descifrar = (fin - inicio) * 1000  # Tiempo transcurrido en milisegundos
    print(Style.RESET_ALL + "\n\033[1mTexto descifrado:\n\033[0m")
    print(Fore.GREEN, texto_descifrado)

    print(Style.RESET_ALL + "\n\033[1m------------------------------Resumen de tiempos------------------------------\033[0m\n")
    print("Tiempo transcurrido (lectura):", tiempo_lectura, "ms")
    print("Tiempo transcurrido (generar clave):", tiempo_generar_clave, "ms")
    print("Tiempo transcurrido (cifrar):", tiempo_cifrar, "ms")
    print("Tiempo transcurrido (descifrar):", tiempo_descifrar, "ms\n")

if __name__ == "__main__":
    main()


