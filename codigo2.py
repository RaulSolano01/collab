def es_primo(numero):
    if numero <= 1:
        return False

    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False

    return True

def nextPrime(n):
    n += 1
    while True:
        if es_primo(n):
            return n
        n += 1

if __name__ == "__main__":
    try:
        numero = int(input("Ingrese un número entero: "))
        if numero <= 1:
            print("Por favor, ingrese un número entero mayor que 1.")
        else:
            siguiente_primo = nextPrime(numero)
            print(f"El primer número primo mayor que {numero} es {siguiente_primo}.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
