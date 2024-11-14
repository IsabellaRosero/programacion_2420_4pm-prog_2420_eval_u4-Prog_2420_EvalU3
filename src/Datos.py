import matplotlib.pyplot as plt # type: ignore

# Se solicita al usuario que ingrese los nombres manualmente
def listar_archivos():
    print("Ingrese los nombres de los archivos separados por comas:")
    archivos = input().split(',')
    
    archivos_modificados = []
    for archivo in archivos:
        archivos_modificados.append(archivo.strip())
    
    print("Archivos ingresados:")
    for archivo in archivos_modificados:
        print(archivo)

# Conteo de las palabras del archivo de texto
def contar_palabras(archivo):
    try:
        with open(archivo, 'r') as f:
            texto = f.read()
            palabras = texto.split()
            print(f"Numero de palabras: {len(palabras)}")
    except FileNotFoundError:
        print("El archivo no ha sido encontrado")

# Hacer que se reemplace una palabra en el archivo 
def reemplazar_palabra(archivo):
    buscar = input("Ingrese la palabra buscar: ")
    reemplazar = input("Ingrese la palabra de reemplazo: ")
    try:
        with open(archivo, 'r') as f:
            texto = f.read()
        texto_modificado = texto.replace(buscar, reemplazar)
        with open(archivo, 'w') as f:
            f.write(texto_modificado)
        print(f"Se reemplazo '{buscar}' por '{reemplazar}'")
    except FileNotFoundError:
        print("Archivo no encontrado")

# Conteo de caracteres en un archivo de texto
def contar_caracteres(archivo):
    try:
        with open(archivo, 'r') as f:
            texto = f.read()
            total_de_caracteres = len(texto)
            caracteres_sin_espacios = len(texto.replace(" ", ""))
            print(f"Total de caracteres con espacios: {total_de_caracteres}")
            print(f"Total de caracteres sin espacios: {caracteres_sin_espacios}")
    except FileNotFoundError:
        print("Archivo no encontrado")

# Mostrar las primeras filas de un archivo CSV
def mostrar_primeras_filas(archivo):
    try:
        with open(archivo, 'r') as f:
            for i in range(150):
                linea = f.readline()
                if not linea:
                    break
                print(linea.strip())
    except FileNotFoundError:
        print("Archivo CSV no fue encontrado")

# Calcular estadísticas de una columna en un archivo CSV
def calcular_estadisticas(archivo):
    columna = input("Ingrese el nombre de la columna: ")
    try:
        with open(archivo, 'r') as f:
            encabezados = f.readline().strip().split(',')
            if columna not in encabezados:
                print(f"La columna '{columna}' no existe")
                return
            indice_columna = encabezados.index(columna)
            datos = []
            for linea in f:
                valores = linea.strip().split(',')
                try:
                    valor = float(valores[indice_columna])
                    datos.append(valor)
                except ValueError:
                    pass
            if datos:
                print(f"Numero de datos: {len(datos)}")
                print(f"Promedio: {sum(datos)/len(datos)}")
                print(f"Maximo: {max(datos)}")
                print(f"Minimo: {min(datos)}")
            else:
                print("No se encontraron datos numéricos")
    except FileNotFoundError:
        print("Archivo CSV no encontrado")

# Graficar una columna de un archivo CSV 
def graficar_columna(archivo):
    columna = input("Ingrese el nombre de la columna: ")
    try:
        with open(archivo, 'r') as f:
            encabezados = f.readline().strip().split(',')
            if columna not in encabezados:
                print(f"La columna '{columna}' no existe")
                return
            indice_columna = encabezados.index(columna)
            datos = []
            for linea in f:
                valores = linea.strip().split(',')
                try:
                    valor = float(valores[indice_columna])
                    datos.append(valor)
                except ValueError:
                    pass
            if datos:
                plt.plot(datos)
                plt.title(f"Gráfica de la columna '{columna}'")
                plt.xlabel("Índice")
                plt.ylabel("Valor")
                plt.show()
            else:
                print("No se encontraron datos numéricos.")
    except FileNotFoundError:
        print("Archivo CSV no encontrado")

# Función principal
def main():
    while True:
        print("\n---- Menú Principal ----")
        print("1. Listar archivos")
        print("2. Procesar archivos de texto(.txt)")
        print("3. Procesar archivo CSV(.csv)")
        print("4. Salir")

        opcion = input("Seleccionar una opción: ")

        if opcion == '1':
            listar_archivos()
        elif opcion == '2':
            archivo = input("Ingrese el nombre del archivo de texto (.txt): ")
            if not archivo.endswith('.txt'):
                print("Ingrese el archivo .txt")
                continue

            print("\n--- Menú para archivo de texto (.txt) ---")
            print("1. Contar número de palabras")
            print("2. Reemplazar una palabra por otra")
            print("3. Contar el número de caracteres")

            opcion_txt = input("Seleccione una opción: ")

            if opcion_txt == '1':
                contar_palabras(archivo)
            elif opcion_txt == '2':
                reemplazar_palabra(archivo)
            elif opcion_txt == '3':
                contar_caracteres(archivo)
            else:
                print("Opción no válida.")

        elif opcion == '3':
            archivo = input("Ingrese el nombre del archivo CSV (.csv): ")
            if not archivo.endswith('.csv'):
                print("Por favor, ingrese un archivo .csv")
                continue

            print("\n--- Menú para archivo CSV (.csv) ---")
            print("1. Mostrar las primeras 15 filas")
            print("2. Calcular estadísticas de una columna")
            print("3. Graficar una columna")

            opcion_csv = input("Seleccione una opción: ")

            if opcion_csv == '1':
                mostrar_primeras_filas(archivo)
            elif opcion_csv == '2':
                calcular_estadisticas(archivo)
            elif opcion_csv == '3':
                graficar_columna(archivo)
            else:
                print("Opción no válida.")

        elif opcion == '4':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
