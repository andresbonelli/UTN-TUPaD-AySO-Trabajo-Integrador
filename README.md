# Calculadora de Promedio Interactivo en Python

El proyecto consiste en un programa en Python que solicita al usuario ingresar números, valida cada entrada y calcula el promedio. 
Este repositorio incluye el archivo de configuracion para ejecutar el programa dentro de un contenedor Docker utilizando una imagen de Python 3.11.

## 📁 Archivos incluidos

- `promedio.py`: Script principal del programa.
- `Dockerfile`: Define el entorno de ejecución en Docker.
- `README.md`: Instrucciones para construir y ejecutar el contenedor.

## 🧰 Requisitos

- [Docker](https://www.docker.com/) instalado.

## ⚙️ Construcción de la imagen Docker

1. Abrir una terminal sobre el directorio raiz.
2. Ejecutar el siguiente comando para construir la imagen Docker:

```bash
docker build -t promedio-interactivo .
```

## ▶️ Ejecución del contenedor

1. Ejecutr el programa de forma interactiva con el siguiente comando:

```bash
docker run -it promedio-interactivo
```
## 🧪 Ejemplo de uso

```commandline
Ingrese números para calcular el promedio. Escriba 'fin' para terminar.
Número 1: 12
Número 2: 8.5
Número 3: error
Entrada no válida. Por favor, ingrese un número o 'fin' para terminar.
Número 3: 15
Número 4: fin

El promedio de los 3 números ingresados es: 11.83
```

## 📌 Observaciones

- El programa valida que cada entrada sea numérica.

- Se permite el ingreso de números enteros o decimales.

- Al finalizar, se muestra el promedio con dos decimales.