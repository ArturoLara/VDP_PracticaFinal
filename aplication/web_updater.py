
from get_text_from_url import get_text_from_url
from BBDD import *
import datetime

import urllib2
from text_data_miner import text_data_miner

from bs4 import BeautifulSoup


#def get_text_from_url(link):
#
#    # Copy all of the content from the provided web page
#    webpage = urllib2.urlopen(link)
#
#
#    soup2 = BeautifulSoup(webpage, "html.parser")
#
#    linkSoup = soup2.findAll("p")
#    list = []
#    for i in linkSoup:
#        list.append(i.text.strip())
#    return list

def web_updater(url):

    try:
        texto = get_text_from_url(url)
    except:
        return [["No se ha podido", "leer la pagina"]]

    now = datetime.datetime.now().strftime("%Y-%m-%d")
    base_datos = gestorBBDD()

    diccionario = {}
    lista_final = []
    for frase in texto:
        lista_repetidas = text_data_miner(frase)
        base_datos.addData(now, lista_repetidas)

        for palabra in lista_repetidas:
            if diccionario.has_key(palabra[0]):
                diccionario[palabra[0]]+=palabra[1]
            else:
                diccionario[palabra[0]] = palabra[1]

    for key in diccionario.keys():
        lista_final.append([key, diccionario[key]])
    return lista_final







