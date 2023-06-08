import time

def encrypt(plain_text, key):
    cipher_text = ""
    for col in range(key):
        current_index = col
        while current_index < len(plain_text):
            cipher_text += plain_text[current_index]
            current_index += key
    return cipher_text

def decrypt(cipher_text, key):
    plain_text = [""] * len(cipher_text)
    col_length = (len(cipher_text) + key - 1) // key

    current_index = 0
    for col in range(key):
        row = 0
        position = col
        while position < len(cipher_text):
            plain_text[position] = cipher_text[current_index]
            current_index += 1
            position += col_length
            row += 1

    return "".join(plain_text)

def run_transposition_cipher(file_path):
    # Leer un archivo con el texto a cifrar
    start_time = time.time()
    with open(file_path, "r") as file:
        plain_text = file.read()
    elapsed_time = (time.time() - start_time) * 1000
    print("Tiempo de lectura del archivo: {:.3f} milisegundos".format(elapsed_time))
    print()

    # Generar y/o imprimir la(s) clave(s) de cifrado
    start_time = time.time()
    key = 5  # Ajusta la clave según tus necesidades
    print("Clave de cifrado:", key)
    elapsed_time = (time.time() - start_time) * 1000
    print("Tiempo de generación de la clave de cifrado: {:.3f} milisegundos".format(elapsed_time))
    print()

    # Cifrar e imprimir el texto cifrado
    start_time = time.time()
    cipher_text = encrypt(plain_text, key)
    elapsed_time = (time.time() - start_time) * 1000
    print("Texto cifrado:")
    print(cipher_text)
    print("Tiempo de cifrado: {:.3f} milisegundos".format(elapsed_time))
    print()

    # Descifrar e imprimir el texto claro
    start_time = time.time()
    decrypted_text = decrypt(cipher_text, key)
    elapsed_time = (time.time() - start_time) * 1000
    print("Texto descifrado:")
    print(decrypted_text)
    print("Tiempo de descifrado: {:.3f} milisegundos".format(elapsed_time))
    print()

file_path = "palabras10.txt"  # Cambiar el nombre del archivo según tus necesidades
run_transposition_cipher(file_path)


