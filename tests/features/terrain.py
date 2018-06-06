from lettuce import world, before, after
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display
@before.all
def setup_browser():
    # world.driver = webdriver.Chrome('chromedriver.exe')

    display = Display(visible=0, size=(800, 800))
    display.start()

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_driver_binary = "/usr/local/bin/chromedriver"
    world.driver = webdriver.Chrome(chrome_driver_binary, chrome_options=chrome_options)
    world.driver.get("http://35.180.103.245:8000/")



@after.all
def close_browser(total):
    world.driver.close()
