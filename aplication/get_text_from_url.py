import urllib2
from text_data_miner import text_data_miner

from bs4 import BeautifulSoup


def get_text_from_url(link):

    # Copy all of the content from the provided web page
    webpage = urllib2.urlopen(link).read()


    soup2 = BeautifulSoup(webpage, "html.parser")

    linkSoup = soup2.findAll("p")
    list = []
    for i in linkSoup:
        list.append(i.text.strip())
    return list


if __name__ == '__main__':
    link = get_text_from_url("https://politica.elpais.com/politica/2018/06/03/actualidad/1528050542_519129.html")
    for i in link:
        print(text_data_miner(i))
