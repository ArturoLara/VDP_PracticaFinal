# -*- coding: UTF-8 -*-
import string
import sys

def text_data_miner(texto):
    # Se codifica a unicode y se decodifica a UTF-8
    reload(sys)  # Reload does the trick!
    sys.setdefaultencoding('UTF8')
    texto = texto.decode().encode()

    if type(texto) is not str:
        raise TypeError

    texto = texto.lower()

    more_puntuation=['¡', '´', '¨', '¿', '«', '»', '©']
    for puntuacion in string.punctuation:
        texto = texto.replace(puntuacion, " ")
    for puntuacion in more_puntuation:
        texto = texto.replace(puntuacion, " ")

    palabras = texto.split()
    stop_words = ['a', 'un', 'una', 'unas', 'unos', 'uno', 'sobre', 'tras', 'otro', 'alguno', 'alguna', 'algunos',
                  'de', 'desde', 'algunas', 'ser', 'es', 'soy', 'eres', 'somos', 'sois', 'estoy', 'esta', 'estamos',
                  'estais', 'hacia', 'estan', 'como', 'en', 'para', 'hasta', 'atras', 'porque', 'por', 'estado',
                  'estaba', 'ante', 'antes', 'siendo', 'ambos', 'pero', 'por', 'poder', 'puede', 'puedo', 'podemos',
                  'podeis', 'contra', 'pueden', 'fui', 'fue', 'fuimos', 'fueron', 'hacer', 'hago', 'hace', 'hacemos',
                  'haceis', 'hacen', 'cada', 'fin', 'incluso', 'primero', 'conseguir', 'consigo', 'consigue',
                  'consigues', 'más', 'conseguimos', 'consiguen', 'ir', 'voy', 'va', 'vamos', 'vais', 'van', 'vaya',
                  'gueno','ha', 'tener', 'tengo', 'tiene', 'tenemos', 'teneis', 'tienen', 'el', 'la', 'lo', 'las',
                  'aqui', 'mio', 'tuyo', 'ellos', 'ellas', 'nos', 'nosotros', 'vosotros', 'vosotras', 'si', 'dentro',
                  'solo', 'solamente', 'saber', 'sabes', 'sabe', 'sabemos', 'sabeis', 'saben', 'ultimo', 'largo',
                  'bastante', 'haces', 'muchos', 'aquellos', 'aquellas', 'sus', 'entonces', 'tiempo', 'verdad',
                  'verdadero', 'verdadera', 'ciertos', 'cierta', 'ciertas', 'intentar', 'intento', 'intenta',
                  'intentas', 'intentamos', 'intentais', 'intentan', 'dos', 'bajo', 'arriba', 'encima', 'usar', 'uso',
                  'usas', 'usa', 'usamos', 'usais', 'usan', 'emplear', 'empleo', 'empleas', 'emplean', 'ampleamos',
                  'empleais', 'valor', 'muy', 'era', 'eras', 'eramos', 'eran', 'modo', 'bien', 'cual', 'cuando',
                  'donde', 'mientras', 'quien', 'con', 'entre', 'sin', 'trabajo', 'trabajar', 'trabajas', 'trabaja',
                  'trabajamos', 'trabajais', 'trabajan', 'podria', 'podrias', 'podriamos', 'podrian', 'podriais',
                  'los', 'su', 'yo', 'aquel']

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
