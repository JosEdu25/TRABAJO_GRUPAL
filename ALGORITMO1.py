#Bubble sort (ordenamiento burbuja)
def Datos():
    # Función para ingresar datos a una lista
    lista = []
    
    while True:
        n = int(input("Ingresa los datos. Usa 0 para terminar: "))
        if n == 0:
            return lista  # Retorna la lista cuando se ingresa 0
        else:
            lista.append(n)  # Agrega el número a la lista si no es 0
    return lista

def burbuja(lista):
    # Implementación del método de ordenamiento burbuja
    tamano = len(lista)
    
    # Bucle externo: recorre la lista para cada pase
    for _ in range(0, tamano):
        
        # Bucle interno: compara y ordena los elementos adyacentes
        for j in range(0, tamano-1):
            if lista[j] > lista[j+1]:
                # Intercambia elementos si están en el orden incorrecto
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
                
    return lista

def mostrarLista(lista):
    # Muestra la lista en orden ascendente y descendente
    tam = len(lista)
    
    print("Orden de manera ascendente:")
    for i in range(0, tam):
        print(f"{lista[i]}")
    
    print("Orden de manera descendente:")
    
    # Bucle inverso: muestra la lista en orden descendente
    for i in range(tam, 0, -1):
        print(f"{lista[i-1]}")

# Ejecución del programa
lista = Datos()
lista = burbuja(lista)
mostrarLista(lista)
