import random
import string

def generar_contraseña_aleatoria():
    longitud = random.randint(7, 10)  # Longitud aleatoria entre 7 y 10 caracteres
    caracteres = string.printable[33:94]  # Caracteres en el rango ASCII 33-126 (sin espacios y caracteres especiales)
    
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

if __name__ == "__main__":
    contraseña_generada = generar_contraseña_aleatoria()
    print(f"Contraseña generada aleatoriamente: {contraseña_generada}")
