import random
import time
import statistics

class ListaOperaciones:
    listas_creadas = []
   

    def __init__(self):
        self.mi_lista = []
        self.tiempo_burbuja = None
        self.tiempo_rapido = None
        ListaOperaciones.listas_creadas.append(self)

    def __str__(self):
        return f"Lista de números: {self.mi_lista}"

    def __len__(self):
        return len(self.mi_lista)

    def mostrar_menu_principal(self):
        while True:
            print("\nMenú Principal:")
            print("1. Generar lista aleatoria")
            print("2. Ingresar lista manualmente")
            print("3. Usar lista previamente cargada")
            print("4. Generar lista desde rango")
            print("5. Ayuda")
            print("6. Salir")

            opcion = input("Elija una opción: ")

            try:
                opcion = int(opcion)
            except ValueError:
                print("Opción no válida. Ingrese un número.")
                continue

            if opcion == 1:
                self.generar_lista_aleatoria()
                self.mostrar_submenu()
            elif opcion == 2:
                self.ingresar_lista_manualmente()
                self.mostrar_submenu()
            elif opcion == 3:
                self.usar_lista_previamente_cargada()
                self.mostrar_submenu()
            elif opcion == 4:
                self.generar_lista_desde_rango()
                self.mostrar_submenu()
            elif opcion == 5:
                self.mostrar_ayuda()
            elif opcion == 6:
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Elija una opción del menú.")

    def generar_lista_aleatoria(self):
        tamano = int(input("Ingrese el tamaño de la lista aleatoria: "))
        self.mi_lista = [random.randint(0, 100000) for _ in range(tamano)]
        print("Lista aleatoria generada.")
        self.mostrar_10_primeros_elementos()

    def ingresar_lista_manualmente(self):
        elementos = input("Ingrese los elementos separados por coma: ").split(",")
        try:
            self.mi_lista = [int(e) for e in elementos]
            print("Lista ingresada manualmente.")
            self.mostrar_10_primeros_elementos()
        except ValueError:
            print("Entrada no válida. Ingrese números separados por coma.")

    def usar_lista_previamente_cargada(self):
        if not self.mi_lista:
            print("No hay una lista previamente cargada.")
        else:
            print("Usando la lista previamente cargada.")
            self.mostrar_10_primeros_elementos()
            self.mostrar_submenu()

    def generar_lista_desde_rango(self):
        inicio = int(input("Ingrese el valor inicial del rango: "))
        fin = int(input("Ingrese el valor final del rango: "))
        tamano = int(input("Ingrese el tamaño de la lista: "))
        self.mi_lista = [random.randint(inicio, fin) for _ in range(tamano)]
        print("Lista generada desde rango.")
        self.mostrar_10_primeros_elementos()

    def mostrar_10_primeros_elementos(self):
        print("Los 10 primeros elementos de la lista son:", self.mi_lista[:10])

    def mostrar_submenu(self):
        while True:
            print("\nSubmenú:")
            print("a. Imprimir lista")
            print("b. Ordenar con burbuja")
            print("c. Ordenar con rápido")
            print("d. Comparar con sorted()")
            print("e. Buscar elemento (búsqueda lineal)")
            print("f. Buscar elemento (búsqueda binaria)")
            print("g. Sumar elementos")
            print("h. Calcular promedio")
            print("i. Calcular mediana")
            print("j. Calcular varianza")
            print("k. Encontrar el mínimo")
            print("l. Encontrar el máximo")
            print("m. Mostrar longitud de la lista")
            print("n. Comparar con otra lista")
            print("o. Volver al menú principal")

            opcion_submenu = input("Elija una opción del submenú: ")

            if opcion_submenu == 'a':
                self.imprimir_lista()
            elif opcion_submenu == 'b':
                self.ordenar_con_burbuja()
            elif opcion_submenu == 'c':
                self.ordenar_con_rapido()
            elif opcion_submenu == 'd':
                self.comparar_con_sorted()
            elif opcion_submenu == 'e':
                self.buscar_elemento_lineal()
            elif opcion_submenu == 'f':
                self.buscar_elemento_binaria()
            elif opcion_submenu == 'g':
                self.sumar_elementos()
            elif opcion_submenu == 'h':
                self.calcular_promedio()
            elif opcion_submenu == 'i':
                self.calcular_mediana()
            elif opcion_submenu == 'j':
                self.calcular_varianza()
            elif opcion_submenu == 'k':
                self.encontrar_minimo()
            elif opcion_submenu == 'l':
                self.encontrar_maximo()
            elif opcion_submenu == 'm':
                self.mostrar_longitud_lista()
            elif opcion_submenu == 'n':
                self.comparar_con_otra_lista()
            elif opcion_submenu == 'o':
                break
            else:
                print("Opción no válida. Elija una opción del submenú.")

    def imprimir_lista(self):
        print("Lista generada (primeros 10 elementos):", self.mi_lista[:10])
        
  
     
    def ordenar_con_burbuja(self):
        lista_ordenada = self.mi_lista.copy()
        start_time = time.time()
        n = len(lista_ordenada)
        for i in range(n):
            for j in range(0, n-i-1):
                if lista_ordenada[j] > lista_ordenada[j+1]:
                    lista_ordenada[j], lista_ordenada[j+1] = lista_ordenada[j+1], lista_ordenada[j]
        end_time = time.time()
        self.tiempo_burbuja = end_time - start_time
        print("Lista ordenada con burbuja (primeros 10 elementos):", lista_ordenada[:10])
        print("Tiempo de ejecución:", end_time - start_time, "segundos")

    def ordenar_con_rapido(self):
        lista_ordenada = self.mi_lista.copy()
        start_time = time.time()
        lista_ordenada = self.quicksort(lista_ordenada)
        end_time = time.time()
        self.tiempo_rapido = end_time - start_time 
        print("Lista ordenada con rápido (primeros 10 elementos):", lista_ordenada[:10])
        print("Tiempo de ejecución:", end_time - start_time, "segundos")
        
       
    
    def comparar_con_sorted(self):
        times = []
        if self.tiempo_burbuja is None or self.tiempo_rapido is None:
            print("Primero debes ejecutar los métodos de burbuja y rápido para hacer el comparativo de tiempo de ejecución con sorted")
            return
        for _ in range(5):
            lista_copia = self.mi_lista.copy()
            start_time = time.time()
            lista_copia.sort()
            end_time = time.time()
            times.append(end_time - start_time)
        print("Tiempo de ejecución con burbuja:", self.tiempo_burbuja, "segundos")
        print("Tiempo de ejecución con rápido:", self.tiempo_rapido, "segundos")
        print("Tiempos de ejecución promedio para ordenar con sorted():", statistics.mean(times), "segundos")

    def buscar_elemento_lineal(self):
        elemento = int(input("Ingrese el elemento a buscar: "))
        for i, num in enumerate(self.mi_lista):
            if num == elemento:
                print("Elemento encontrado en la posición", i)
                return
        print("Elemento no encontrado.")

    def buscar_elemento_binaria(self):
        if not self.mi_lista:
            print("La lista está vacía.")
            return

        elemento = int(input("Ingrese el elemento a buscar: "))
        self.mi_lista.sort()

        start_time = time.time()
        left, right = 0, len(self.mi_lista) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.mi_lista[mid] == elemento:
                print("Elemento encontrado en la posición", mid)
                return
            elif self.mi_lista[mid] < elemento:
                left = mid + 1
            else:
                right = mid - 1
        print("Elemento no encontrado.")

    def sumar_elementos(self):
        suma = sum(self.mi_lista)
        print("Suma de elementos:", suma)

    def calcular_promedio(self):
        if len(self.mi_lista) > 0:
            promedio = sum(self.mi_lista) / len(self.mi_lista)
            print("Promedio:", promedio)
        else:
            print("La lista está vacía.")

    def calcular_mediana(self):
        if len(self.mi_lista) > 0:
            mediana = statistics.median(self.mi_lista)
            print("Mediana:", mediana)
        else:
            print("La lista está vacía.")

    def calcular_varianza(self):
        if len(self.mi_lista) > 0:
            varianza = statistics.variance(self.mi_lista)
            print("Varianza:", varianza)
        else:
            print("La lista está vacía.")

    def encontrar_minimo(self):
        if len(self.mi_lista) > 0:
            minimo = min(self.mi_lista)
            print("Mínimo de la lista:", minimo)
        else:
            print("La lista está vacía.")

    def encontrar_maximo(self):
        if len(self.mi_lista) > 0:
            maximo = max(self.mi_lista)
            print("Máximo de la lista:", maximo)
        else:
            print("La lista está vacía.")

    def mostrar_longitud_lista(self):
        longitud = len(self.mi_lista)
        print("Longitud de la lista:", longitud)
        
        
    """@classmethod
    def comparar_todas_con_otra_lista(cls, otra_lista):
        listas_iguales = []
        for lista in cls.listas_creadas:
            if lista.mi_lista == otra_lista:
                listas_iguales.append(lista)
        
        if not listas_iguales:
            print("No hay listas que sean iguales a la lista proporcionada.")
        else:
            print("Las siguientes listas son iguales a la lista proporcionada:")
            for lista in listas_iguales:
                print(f"Lista en la instancia {lista}:", lista.mi_lista)"""

    def comparar_con_otra_lista(self):
        otra_lista = input("Ingrese otra lista de números separados por coma: ").split(",")
        try:
            otra_lista = [int(e) for e in otra_lista]
        except ValueError:
            print("Entrada no válida. Ingrese números separados por coma.")
            return

        if self.mi_lista == otra_lista:
            print("Las listas son iguales.")
        else:
            print("Las listas no son iguales.")

    @staticmethod
    def quicksort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return ListaOperaciones.quicksort(left) + middle + ListaOperaciones.quicksort(right)

    def mostrar_ayuda(self):
        print("\nAyuda:")
        print("Este programa le permite realizar diversas operaciones en una lista de números.")
        print("Puede generar una lista aleatoria, ingresar una lista manualmente, usar una lista previamente cargada")
        print("o generar una lista desde un rango específico.")
        print("Luego, puede realizar varias operaciones en la lista, como ordenar, buscar, calcular estadísticas, etc.")

if __name__ == "__main__":
    menu = ListaOperaciones()
    menu.mostrar_menu_principal()