def busqueda_lineal(lista, objetivo):
    for indice, elemento in enumerate(lista):
        if elemento == objetivo:
            return indice
    return -1


def busqueda_binaria(lista, objetivo):
    lista.sort()
    
    bajo = 0
    alto = len(lista) - 1
    
    while bajo <= alto:
        medio = (bajo + alto) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    return -1


if __name__ == "__main__":
    import time

    lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    objetivo = 19

    # Prueba Búsqueda Lineal
    start_time = time.time()
    resultado_lineal = busqueda_lineal(lista, objetivo)
    end_time = time.time()
    tiempo_lineal = end_time - start_time
    print(f"Búsqueda Lineal: índice {resultado_lineal}, tiempo {tiempo_lineal:.6f} segundos")

    # Prueba Búsqueda Binaria
    start_time = time.time()
    resultado_binario = busqueda_binaria(lista, objetivo)
    end_time = time.time()
    tiempo_binario = end_time - start_time
    print(f"Búsqueda Binaria: índice {resultado_binario}, tiempo {tiempo_binario:.6f} segundos")
