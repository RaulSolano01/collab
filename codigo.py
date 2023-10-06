def es_primo(numero):
    if numero <= 1:
        return False  # Los números menores o iguales a 1 no son primos

    # Comprobar si el número es divisible por algún número en el rango
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False  # El número es divisible, por lo que no es primo

    return True  # Si no se encontraron divisores, el número es primo

if __name__ == "__main__":
    try:
        numero = int(input("Ingrese un número entero mayor que 1: "))
        if numero <= 1:
            print("Por favor, ingrese un número entero válido mayor que 1.")
        elif es_primo(numero):
            print(f"{numero} es un número primo.")
        else:
            print(f"{numero} no es un número primo.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
