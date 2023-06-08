import time
import random
import colorsys

inilec=0
finilec=0
inicif=0
finicif=0
inides=0
finides=0
inicl=0
finicl=0


def cifrado_cesar(texto, desplazamiento):
    global inicif
    inicif=time.time()
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            codigo = ord(caracter)
            if caracter.isupper():
                codigo = (codigo - 65 + desplazamiento) % 27 + 65
            else:
                codigo = (codigo - 97 + desplazamiento) % 27 + 97
            caracter_cifrado = chr(codigo)
            resultado += caracter_cifrado
        else:
            resultado += caracter
    global finicif
    finicif=time.time()
    return resultado



def descifrado_cesar(texto, desplazamiento):
    global inides
    inides=time.time()
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            codigo = ord(caracter)
            if caracter.isupper():
                codigo = (codigo - 65 - desplazamiento) % 27 + 65
            else:
                codigo = (codigo - 97 - desplazamiento) % 27 + 97
            caracter_descifrado = chr(codigo)
            resultado += caracter_descifrado
        else:
            resultado += caracter
    global finides
    finides=time.time()
    return resultado
    

def generar_clave():
    global inicl
    inicl=time.time()
    return random.randint(1, 26)
finicl=time.time()
    

desplazamiento = generar_clave()

def leer(path,cant):
    global inilec
    inilec=time.time()
    with open (path) as file_object:
        leer = file_object.read()
    global finilec
    finilec=time.time()
    print(f"esta es un cifrado por sustitucion a un archivo de {cant} palabras")
    print("el texto es:")
    print("")
    print(leer)
    print("")
    print("-----------------------------------------------------------------")
    ccesar = cifrado_cesar(leer,desplazamiento)
    print(f"la clave de cifrado es +{desplazamiento}")
    print("el texto cifrado es:")
    print("")
    print(ccesar)
    print("")
    print("------------------------------------------------------------------")
    dcesar = descifrado_cesar(ccesar, desplazamiento)
    print(f"la clave de descifrado es -{desplazamiento}")
    print("el texto descifrado es")
    print("")
    print(dcesar)
    print("")
    print("--------------------------------------------------------------------")

while True:
    print("")
    print("")
    print("BIENVENIDO CIFRADO POR SUSTITUCION")
    print("-----------------------------------")
    print("1.- 10 palabras")
    print("2.- 100 palabras")
    print("3.- 1000 palabras")
    print("4.- 10000 palabras")
    print("5.- 100000 palabras")
    print("6.- 1000000 palabras")
    print("7.- salir")
    opcion = int(input())
    if (opcion==1):
        path="10.txt"
        cant="diez"
        leer(path,cant)
        tiempolec=(finilec-inilec)*1000
        tiempocif=(finicif-inicif)*1000
        tiempodes=(finides-inides)*1000
        tiempocl=(finicl-inicl)*1000
        print("TIEMPO TRANSCURRIDO")
        print("")
        print(f"El tiempo para generar la clave de cifrado fue {round(tiempocl,3)}")
        print(f"el tiempo para leer el texto fue {round(tiempolec,3)} ms")
        print(f"el tiempo para cifrar el texto fue {round(tiempocif,3)} ms")
        print(f"el tiempo para descifrar el texto fue {round(tiempodes,3)} ms")
        
    elif opcion==2:
        path="100.txt"
        cant="cien"
        leer(path,cant)
        tiempolec=(finilec-inilec)*1000
        tiempocif=(finicif-inicif)*1000
        tiempodes=(finides-inides)*1000
        tiempocl=(finicl-inicl)*1000
        print("TIEMPO TRANSCURRIDO")
        print("")
        print(f"El tiempo para generar la clave de cifrado fue {round(tiempocl,3)}")
        print(f"el tiempo para leer el texto fue {round(tiempolec,3)} ms")
        print(f"el tiempo para cifrar el texto fue {round(tiempocif,3)} ms")
        print(f"el tiempo para descifrar el texto fue {round(tiempodes,3)} ms")
        
    elif opcion==3:
        path="1000.txt"
        cant="mil"
        leer(path,cant)
        tiempolec=(finilec-inilec)*1000
        tiempocif=(finicif-inicif)*1000
        tiempodes=(finides-inides)*1000
        tiempocl=(finicl-inicl)*1000
        print("TIEMPO TRANSCURRIDO")
        print("")
        print(f"El tiempo para generar la clave de cifrado fue {round(tiempocl,3)}")
        print(f"el tiempo para leer el texto fue {round(tiempolec,3)} ms")
        print(f"el tiempo para cifrar el texto fue {round(tiempocif,3)} ms")
        print(f"el tiempo para descifrar el texto fue {round(tiempodes,3)} ms")
    elif opcion==4:
        path="10000.txt"
        cant="diez mil"
        leer(path,cant)
        tiempolec=(finilec-inilec)*1000
        tiempocif=(finicif-inicif)*1000
        tiempodes=(finides-inides)*1000
        tiempocl=(finicl-inicl)*1000
        print("TIEMPO TRANSCURRIDO")
        print("")
        print(f"El tiempo para generar la clave de cifrado fue {round(tiempocl,3)}")
        print(f"el tiempo para leer el texto fue {round(tiempolec,3)} ms")
        print(f"el tiempo para cifrar el texto fue {round(tiempocif,3)} ms")
        print(f"el tiempo para descifrar el texto fue {round(tiempodes,3)} ms")
    elif opcion==5:
        path="100000.txt"
        cant="cien mil"
        leer(path,cant)
        tiempolec=(finilec-inilec)*1000
        tiempocif=(finicif-inicif)*1000
        tiempodes=(finides-inides)*1000
        tiempocl=(finicl-inicl)*1000
        print("TIEMPO TRANSCURRIDO")
        print("")
        print(f"El tiempo para generar la clave de cifrado fue {round(tiempocl,3)}")
        print(f"el tiempo para leer el texto fue {round(tiempolec,3)} ms")
        print(f"el tiempo para cifrar el texto fue {round(tiempocif,3)} ms")
        print(f"el tiempo para descifrar el texto fue {round(tiempodes,3)} ms")
    elif opcion==6:
        path="1000000.txt"
        cant="un millon"
        leer(path,cant)
        tiempolec=(finilec-inilec)*1000
        tiempocif=(finicif-inicif)*1000
        tiempodes=(finides-inides)*1000
        tiempocl=(finicl-inicl)*1000
        print("TIEMPO TRANSCURRIDO")
        print("")
        print(f"El tiempo para generar la clave de cifrado fue {round(tiempocl,3)}")
        print(f"el tiempo para leer el texto fue {round(tiempolec,3)} ms")
        print(f"el tiempo para cifrar el texto fue {round(tiempocif,3)} ms")
        print(f"el tiempo para descifrar el texto fue {round(tiempodes,3)} ms")
    elif opcion==7:
        break
    else:
        print("seleccione una opcion valida")

