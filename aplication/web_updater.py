from text_data_miner import text_data_miner
from get_text_from_url import get_text_from_url
from BBDD import *
import datetime



def web_updater(url):

    try:
        texto = get_text_from_url(url)
    except:
        return [["No se ha podido", "leer la pagina"]]

    now = datetime.datetime.now().strftime("%Y-%m-%d")
    base_datos = gestorBBDD()

    for frase in texto:
        lista_repetidas = text_data_miner(frase)
        print(lista_repetidas)
        base_datos.addData(now, lista_repetidas)


    return base_datos.showData(now)


if __name__ == '__main__':
    print(web_updater("http://www.elmundo.es/cultura/2017/03/09/58c063b4ca4741e2268b45ba.html"))




