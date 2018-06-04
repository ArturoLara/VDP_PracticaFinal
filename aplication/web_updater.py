from text_data_miner import text_data_miner
from get_text_from_url import get_text_from_url

def web_updater(url):

    try:
        texto = get_text_from_url(url)
    except:
        return "No se ha podido leer la pagina"

    diccionario = {}
    lista = [[]]
    for frase in texto:
        lista_repetidas = text_data_miner(frase)

        #for element in lista_repetidas:
        #    if element[0] in diccionario.keys():
        #        diccionario[element[0]] += element[1]
        #    else:
        #        diccionario[element[0]] = element[1]

        #llamar a arturo con cada frase
        #recibir los datos
    return diccionario


if __name__ == '__main__':
    print(web_updater("http://www.elmundo.es/cultura/2017/03/09/58c063b4ca4741e2268b45ba.html"))




