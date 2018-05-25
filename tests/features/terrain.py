from lettuce import world, before, after
from selenium import webdriver


@before.all
def setup_browser():
    # world.driver = webdriver.Chrome('chromedriver.exe')
    world.driver = webdriver.Chrome()
    world.driver.get("http://127.0.0.1:8000/")


@after.all
def close_browser(total):
    world.driver.close()
