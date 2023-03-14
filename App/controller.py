"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
# TODO: lab 7, import para medir tiempo y memoria
import time
import tracemalloc
import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def newController():
    """
    Crea una instancia del modelo
    """
    control = {
        'model': None
    }
    control['model'] = model.newCatalog()
    return control


# Funciones para la carga de datos


def loadData(control, memflag=True):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    # TODO: lab 7, implementacion del catalogo midiendo el tiempo y memoria
    # toma el tiempo al inicio del proceso
    start_time = getTime()

    # inicializa el proceso para medir memoria
    if memflag is True:
        tracemalloc.start()
        start_memory = getMemory()

    loadBooks(control)
    loadTags(control)
    loadBooksTags(control)

    # toma el tiempo al final del proceso
    stop_time = getTime()
    # calculando la diferencia en tiempo
    delta_time = deltaTime(stop_time, start_time)

    # finaliza el proceso para medir memoria
    if memflag is True:
        stop_memory = getMemory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        delta_memory = deltaMemory(stop_memory, start_memory)
        # respuesta con los datos de tiempo y memoria
        return delta_time, delta_memory

    else:
        # respuesta sin medir memoria
        return delta_time


def loadBooks(control):
    """
    Carga los libros del archivo. Por cada libro se indica al
    modelo que debe adicionarlo al catalogo.
    """
    booksfile = cf.data_dir + 'GoodReads/books.csv'
    input_file = csv.DictReader(open(booksfile, encoding='utf-8'))
    for book in input_file:
        model.addBook(control['model'], book)


def loadTags(control):
    """
    Carga todos los tags del archivo e indica al modelo
    que los adicione al catalogo
    """
    tagsfile = cf.data_dir + 'GoodReads/tags.csv'
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    for tag in input_file:
        model.addTag(control['model'], tag)


def loadBooksTags(control):
    """
    Carga la información que asocia tags con libros en el catalogo
    """
    booktagsfile = cf.data_dir + 'GoodReads/book_tags.csv'
    input_file = csv.DictReader(open(booktagsfile, encoding='utf-8'))
    for booktag in input_file:
        model.addBookTag(control['model'], booktag)


# Funciones de consulta sobre el catálogo


def getBestBooks(control, number):
    """
    Retorna los mejores libros según su promedio
    """
    bestbooks = model.getBestBooks(control['model'], number)
    return bestbooks


def countBooksByTag(control, tag):
    """
    Retorna los libros que fueron etiquetados con el tag
    """
    return model.countBooksByTag(control['model'], tag)


def booksSize(control):
    """
    Numero de libros cargados al catalogo
    """
    return model.booksSize(control['model'])


def authorsSize(control):
    """
    Numero de autores cargados al catalogo
    """
    return model.authorsSize(control['model'])


def tagsSize(control):
    """
    Numero de tags cargados al catalogo
    """
    return model.tagsSize(control['model'])


def getBooksByAuthor(control, authorname):
    """
    Retorna los libros de un autor
    """
    authorinfo = model.getBooksByAuthor(control['model'], authorname)
    return authorinfo


def getBooksByTag(control, tagname):
    """
    Retorna los libros que han sido marcados con
    una etiqueta
    """
    books = model.getBooksByTag(control['model'], tagname)
    return books


def getBooksYear(control, year, memflag=True):
    """
    Retorna los libros que fueron publicados
    en un año
    """
    # TODO: lab 7, implementacion de una funcion midiendo el tiempo y memoria
    # respuesta de la funcion
    books = None

    # toma el tiempo al inicio del proceso
    start_time = getTime()

    # inicializa el proceso para medir memoria
    if memflag is True:
        tracemalloc.start()
        start_memory = getMemory()

    # ejecutando funcion a medir
    books = model.getBooksByYear(control['model'], year)

    # toma el tiempo al final del proceso
    stop_time = getTime()
    # calculando la diferencia en tiempo
    delta_time = deltaTime(stop_time, start_time)

    # finaliza el proceso para medir memoria
    if memflag is True:
        stop_memory = getMemory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        delta_memory = deltaMemory(stop_memory, start_memory)
        # respuesta con los datos de tiempo y memoria
        return books, delta_time, delta_memory

    else:
        # respuesta sin medir memoria
        return books, delta_time


def sortBooksByYear(control, year, rank, memflag=True):
    """
    Retorna los libros que fueron publicados
    en un año ordenados por rating
    """
    # TODO lab 7, completar cambios para medir tiempo y memoria
    pass


# Funciones para medir tiempos de ejecucion


def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def deltaTime(end, start):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed


# Funciones para medir la memoria utilizada


def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def deltaMemory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
