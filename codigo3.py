def mediana_de_tres(val1, val2, val3):
    # Ordenar los tres valores de menor a mayor
    valores = [val1, val2, val3]
    valores.sort()
    
    # La mediana es el valor en la posición central
    mediana = valores[1]
    return mediana

if __name__ == "__main__":
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        num3 = float(input("Ingrese el tercer número: "))

        mediana = mediana_de_tres(num1, num2, num3)
        print(f"La mediana de los números ingresados es: {mediana}")
    except ValueError:
        print("Por favor, ingrese tres valores numéricos válidos.")