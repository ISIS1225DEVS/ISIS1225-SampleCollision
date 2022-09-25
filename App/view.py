"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones  y  por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

# Inicializacion de la comunicacion con el controlador


def newController():
    """
    Se crea una instancia del controlador
    """
    control = controller.newController()
    return control


# ===================================
# Funciones para imprimir resultados
# ===================================


def printAuthorData(author):
    """
    Imprime la información del autor seleccionado
    """
    if author:
        print('Autor encontrado: ' + author['name'])
        print('Promedio: ' + str(author['average_rating']))
        print('Total de libros: ' + str(lt.size(author['books'])))
        for book in lt.iterator(author['books']):
            print('Titulo: ' + book['title'] + '  ISBN: ' + book['isbn'])
        print("\n")
    else:
        print('No se encontro el autor.\n')


def printBooksbyTag(books):
    """
    Imprime los libros que han sido clasificados con
    una etiqueta
    """
    if (books):
        print('Se encontraron: ' + str(lt.size(books)) + ' Libros.')
        for book in lt.iterator(books):
            print(book['title'])
        print("\n")
    else:
        print("No se econtraron libros.\n")


def printBooksbyYear(answer):
    """
    Imprime los libros que han sido publicados en un
    año
    """
    if isinstance(answer, (list, tuple)) is True:
        if len(answer) == 2:
            books = answer[0]
            time = answer[1]
            print('Se encontraron: ' + str(lt.size(books)) + ' Libros.')
            print("Tiempo [ms]: ", f"{time:.3f}")
        elif len(answer) == 3:
            books = answer[0]
            time = answer[1]
            memory = answer[2]
            print('Se encontraron: ' + str(lt.size(books)) + ' Libros.')
            print('Tiempo [ms]: ', f"{time:.3f}", '||',
                  'Memoria [kB]: ', f"{memory:.3f}")
        print("Imprimiendo los 3 primeros y 3 ultimos libros...")
        i = 1
        for book in lt.iterator(books):
            if i <= 3 or i > lt.size(books) - 3:
                print('Titulo:', book['title'],
                      'ISBN:', book['isbn'],
                      'Rating:', book['average_rating'])
            i += 1
        print("\n")
    else:
        print("No se encontraron libros.\n")


def printBestBooks(books):
    """
    Imprime la información de los mejores libros
    por promedio
    """
    # TODO: lab 7, implementar la impresión de ranking de libros
    if isinstance(answer, (list, tuple)) is True:
        if len(answer) == 2:
            books = answer[0]
            time = answer[1]
            print("Tiempo [ms]: ", f"{time:.3f}")
        elif len(answer) == 3:
            books = answer[0]
            time = answer[1]
            memory = answer[2]
            print('Tiempo [ms]: ', f"{time:.3f}", '||',
                  'Memoria [kB]: ', f"{memory:.3f}")
        size = lt.size(books)
        if size:
            print(' Estos son los mejores libros: ')
            for book in lt.iterator(books):
                print('Titulo:', book['title'],
                      'ISBN:', book['isbn'],
                      'Rating:', book['average_rating'])
            print("\n")
    else:
        print("No se encontraron libros.\n")


def printLoadDataAnswer(answer):
    """
    Imprime los datos de tiempo y memoria de la carga de datos
    """
    if isinstance(answer, (list, tuple)) is True:
        print("Tiempo [ms]: ", f"{answer[0]:.3f}", "||",
              "Memoria [kB]: ", f"{answer[1]:.3f}")
    else:
        print("Tiempo [ms]: ", f"{answer:.3f}")


def castBoolean(value):
    """
    Convierte un valor a booleano
    """
    if value in ('True', 'true', 'TRUE', 'T', 't', '1', 1, True):
        return True
    else:
        return False


# Menu de opciones


def printMenu():
    print("Bienvenido")
    print("1- Inicializar Catálogo")
    print("2- Cargar información en el catálogo")
    print("3- Consultar los libros de un año")
    print("4- Consultar los libros de un autor")
    print("5- Consultar los Libros por etiqueta")
    print("6- Ordenar mejores libros de un año")
    print("0- Salir")

# ===================================
# Funciones de inicializacion
# ===================================


def initCatalog():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog()


def loadData(catalog):
    """
    Carga los libros en el catalogo
    """
    controller.loadData(catalog)


ctrlr = None
# ===================================
# Menu principal
# ===================================

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs[0]) == 1:
        print("Inicializando Catálogo ....")
        ctrlr = newController()

    elif int(inputs[0]) == 2:
        # TODO: lab 7, parametros para observar el tiempo y memoria
        print("Cargando información de los archivos ....")
        print("Desea observar el uso de memoria? (True/False)")
        mem = input("Respuesta: ")
        mem = castBoolean(mem)
        answer = controller.loadData(ctrlr, memflag=mem)
        print('Libros cargados: ' + str(controller.booksSize(ctrlr)))
        print('Autores cargados: ' + str(controller.authorsSize(ctrlr)))
        print('Géneros cargados: ' + str(controller.tagsSize(ctrlr)))
        printLoadDataAnswer(answer)

    elif int(inputs[0]) == 3:
        # TODO: lab 7, parametros observar el tiempo y memoria
        number = input("Buscando libros del año?: ")
        print("Desea observar el uso de memoria? (True/False)")
        mem = input("Respuesta: ")
        mem = castBoolean(mem)
        answer = controller.getBooksYear(ctrlr, int(number), memflag=mem)
        printBooksbyYear(answer)

    elif int(inputs[0]) == 4:
        authorname = input("Nombre del autor a buscar: ")
        authorinfo = controller.getBooksByAuthor(ctrlr, authorname)
        printAuthorData(authorinfo)

    elif int(inputs[0]) == 5:
        label = input("Etiqueta a buscar: ")
        books = controller.getBooksByTag(ctrlr, label)
        printBooksbyTag(books)

    elif int(inputs[0]) == 6:
        number = input("Buscando libros del año?: ")
        rank = input("Cuantos libros en el escalafon? (mayor a 0): ")
        number = int(number)
        rank = int(rank)
        print("Desea observar el uso de memoria? (True/False)")
        mem = input("Respuesta: ")
        mem = castBoolean(mem)
        # TODO lab 7, completar cambios para imprimir respuesta
        answer = controller.sortBooksByYear(ctrlr, number, rank, memflag=mem)
        printBestBooks(answer)

    elif int(inputs[0]) == 0:
        break

    else:
        continue
sys.exit(0)
