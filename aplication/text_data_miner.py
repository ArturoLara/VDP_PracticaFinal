# !/usr/bin/python
# -*- coding: UTF-8 -*-
import unicodedata


def text_data_miner(texto):

    # Se codifica a unicode y se decodifica a UTF-8
    texto = texto.encode('ascii','ignore')

    if type(texto) is not str:
        raise TypeError

    signos_puntuacion = [",", ".", ";", ":", "?", "¿", "!", "¡", "(", ")", "[", "]", "_", "-", "\"", "/", "*", "'", "´",
                         "`", "+", "¨"]

    for puntuacion in signos_puntuacion:
        texto = texto.replace(puntuacion, " ")


    palabras = texto.split()

    for i in range(len(palabras)):
        palabras[i] = palabras[i].lower()

    with open("aplication/stop_words.txt") as stops:
        stop_words = stops.readline().split()
        stops.close()

    for stops in stop_words:
        while stops in palabras:
            palabras.remove(stops)

    if len(palabras) == 0:
        return ""
    diccionario_repetidos = {}
    for palabra in palabras:
        if palabra in diccionario_repetidos.keys():
            diccionario_repetidos[palabra] += 1
        else:
            diccionario_repetidos[palabra] = 1

    lista_palabras_repetidas = []
    for key in diccionario_repetidos.keys():
        lista_palabras_repetidas.append([key, diccionario_repetidos[key]])


    return sorted(lista_palabras_repetidas, key=lambda tup: tup[1], reverse=True)


if __name__ == '__main__':
    print(text_data_miner("Hola, me llamo Alfonso. Hola que tal, no me llamo Arturo."))
