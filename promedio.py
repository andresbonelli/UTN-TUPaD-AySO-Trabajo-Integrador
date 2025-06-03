def main():
    print("Bienvenido al programa de calcular promedio.")
    print("--------------------------------------------")
    print("Ingrese los números de a uno por vez o 'fin' para terminar y mostrar el resultado.")
    numeros = []
    contador = 1
    while True:
        entrada = input(f"Número {contador}: ").strip()
        if entrada.lower() == "fin":
            break
        try:
            numeros.append(float(entrada))
        except ValueError:
            print("Entrada no válida. Ingrese un número válido o 'fin' para terminar.")
            continue
        contador += 1
    if len(numeros) > 0:
        promedio = sum(numeros) / len(numeros)
        print(f"\nEl promedio de los {len(numeros)} números ingresados es: {promedio:.2f}")
    else:
        print("No se ingresaron números válidos.")

if __name__ == "__main__":
    main()
