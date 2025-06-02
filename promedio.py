from csv import excel


def es_numero(val):
    try:
        float(val)
        return True
    except ValueError:
        return False

def main():
    print("Ingrese números para calcular el promedio (cualquier otro caracter para terminar).")
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
