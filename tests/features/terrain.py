from lettuce import world, before, after
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import mock

def mock_return(url):
    if(url=="invalidUrl"):
        return [["No se ha podido", "leer la pagina"]]
    return [["m2", 2], ["llamo", 2], ["hola", 2]]



@before.all
def setup_browser():
    # world.driver = webdriver.Chrome('chromedriver.exe')
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    world.driver = webdriver.Chrome(chrome_options=chrome_options)
    world.driver.get("http://127.0.0.1:8000/")



@after.all
def close_browser(total):
    world.driver.close()
