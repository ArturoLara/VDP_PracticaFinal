from lettuce import world, before, after
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@before.all
def setup_browser():
    # world.driver = webdriver.Chrome('chromedriver.exe')
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    world.driver = webdriver.Chrome(chrome_options=chrome_options)
    world.driver.get("http://35.180.103.245:8000/")



@after.all
def close_browser(total):
    world.driver.close()
