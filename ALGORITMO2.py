import time
import random

def separacion(lista):
    if len(lista) < 1:
        return [], [], []

    izquierda = []
    derecha = []
    pivote = lista[0]

    for i in range(1, len(lista)):
        if lista[i] < pivote:
            izquierda.append(lista[i])
        else:
            derecha.append(lista[i])

    return izquierda, pivote, derecha

def quickSort(lista):
    if len(lista) < 2:
        return lista
    izquierda, pivote, derecha = separacion(lista)

    return quickSort(izquierda) + [pivote] + quickSort(derecha)

def generar_ordenar_aleatorios(cantidad):
    numeros_aleatorios = [random.randint(0, 200000) for _ in range(cantidad)]
    print("Números aleatorios generados:", numeros_aleatorios)
    return quickSort(numeros_aleatorios)

def generarNumerosAleatorios(n, limite):
    return [random.randint(1, limite) for _ in range(n)]

def ordenPorSeleccion(lista):
    tamaño = len(lista)
    for i in range(0, tamaño):
        min_index = i
        for j in range(i+1, tamaño):
            if lista[min_index] > lista[j]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista

def mostrarLista(lista):
    for numero in lista:
        print(numero)

def insertion_sort(arr, reverse=False):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and ((key > arr[j]) if reverse else (key < arr[j])):
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

def generar_datos(cantidad, limite):
    return [random.randint(1, limite) for _ in range(cantidad)]

def bubble_sort(lista):
    tamaño = len(lista)
    
    for _ in range(0, tamaño):
        for j in range(0, tamaño-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista

# Ejemplo de uso para cada algoritmo

cantidad_numeros = int(input("Ingrese la cantidad limite: "))
limite_superior = int(input("Ingrese el número límite para los números aleatorios: "))

# QuickSort
lista_quick_sort = generar_datos(cantidad_numeros, limite_superior)
tiempo_inicio_quick_sort = time.time()
quickSort(lista_quick_sort)
tiempo_fin_quick_sort = time.time()
print(f"QuickSort: Tiempo de ejecución {tiempo_fin_quick_sort - tiempo_inicio_quick_sort} segundos")

# Selección
lista_seleccion = generar_datos(cantidad_numeros, limite_superior)
tiempo_inicio_seleccion = time.time()
ordenPorSeleccion(lista_seleccion)
tiempo_fin_seleccion = time.time()
print(f"Selección: Tiempo de ejecución {tiempo_fin_seleccion - tiempo_inicio_seleccion} segundos")

# Inserción
lista_insercion = generar_datos(cantidad_numeros, limite_superior)
tiempo_inicio_insercion = time.time()
insertion_sort(lista_insercion)
tiempo_fin_insercion = time.time()
print(f"Inserción: Tiempo de ejecución {tiempo_fin_insercion - tiempo_inicio_insercion} segundos")

# Burbuja
lista_burbuja = generar_datos(cantidad_numeros, limite_superior)
tiempo_inicio_burbuja = time.time()
bubble_sort(lista_burbuja)
tiempo_fin_burbuja = time.time()
print(f"Burbuja: Tiempo de ejecución {tiempo_fin_burbuja - tiempo_inicio_burbuja} segundos")
