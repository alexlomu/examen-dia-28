from csv import reader

def junta_csv(csv/starships.csv, archivos):
    """
    Crea un archivo .csv a partir de multiples
    archivos .csv con una sola columna

    :param salida: Nombre del archivo de salida.
    :param archivos: Lista de archivos de entrada.
                     Son .csv con header en la primera fila.
    """
    handles = [] # Archivos de entrada
    headers = [] # Headers de cada archivo de entrada
    #
    #   Abrir los archivos de entradas, leer los headers
    #
    for arch in archivos:
        file_handle = open(arch, "r")
        handles.append(file_handle)
        headers.append(file_handle.readline().strip())

    with open(salida, "w") as out:
        #   Formar la primera linea con los headers de
        #   las columnas.
        header = ",".join(headers)
        out.write(f"{header}\n")

        eof = False
        while not eof:
            fila = []
            #   Leer una fila de cada archivo para
            #   formar una fila de salida.
            for handle in handles:
                dato = handle.readline()
                if dato:
                    fila.append(dato.strip())
                else:
                    eof = True
                    break

            if not eof:
                #   Grabar la fila de salida.
                salida = ','.join(fila)
                out.write(f"{salida}\n")

    #   Cerrar tosdos los archivos
    out.close()
    for handle in handles:
        handle.close()

with open('Employees.csv', 'r') as csv_file:
    csv_reader = reader(csv_file)
    # Passing the cav_reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)
    print(list_of_rows)