from lettuce import world, before, after
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from mock import patch


@before.all
@patch('aplication.web_updater.web_updater')
def setup_browser(some_function):
    # world.driver = webdriver.Chrome('chromedriver.exe')
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    some_function.return_value = [["m2", 2], ["llamo", 2], ["hola", 2]]

    world.driver = webdriver.Chrome(chrome_options=chrome_options)
    world.driver.get("http://127.0.0.1:8000/")



@after.all
def close_browser(total):
    world.driver.close()
