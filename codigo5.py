def calcular_hipotenusa(lado1, lado2):
    hipotenusa = (lado1**2 + lado2**2)**0.5
    return hipotenusa

if __name__ == "__main__":
    try:
        lado1 = float(input("Ingrese la longitud del primer lado corto: "))
        lado2 = float(input("Ingrese la longitud del segundo lado corto: "))

        hipotenusa = calcular_hipotenusa(lado1, lado2)
        print(f"La longitud de la hipotenusa es: {hipotenusa}")
    except ValueError:
        print("Por favor, ingrese longitudes válidas de los lados cortos del triángulo rectángulo.")