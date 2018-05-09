from lettuce import step
from lettuce import world, before, after
from selenium import webdriver

@before.all
def setup_browser():
    world.driver = webdriver.Chrome('chromedriver.exe')
    world.driver.get("http://127.0.0.1:8000/")

@after.all
def close_browser(total):
    world.driver.close()


@step('I have the text "(.*)"')
def have_the_text(step, text):
    world.text = text

@step('I put it in the textfild')
def put_text_click_e_bottom(step):
    world.driver.find_element_by_id("id_text").send_keys(world.text)

@step('I see the result text "(.*)" and "(.*)" in the textfield')
def check_result_text(step, textResult, textfield):
    world.driver.find_element_by_id("execute").click()
    web_text = world.driver.find_element_by_id("id_text").get_attribute('value')
    result_text = world.driver.find_element_by_id("answer").text
    assert web_text == textfield and result_text == textResult

@step('I click the reset bottom')
def click_r_buttom(step):
    world.driver.find_element_by_id("reset").click()

@step('I have in the textfield the text "(.*)"')
def put_text_at_textfield(step, text):
    world.driver.find_element_by_id("id_text").send_keys(text)

@step('I put it in the textfield')
def put_saved_text_at_textfield(step):
    world.driver.find_element_by_id("id_text").send_keys(world.text)

@step('I see in the textfield the text "(.*)"')
def check_text(step, text):
    textfield = world.driver.find_element_by_id("id_text").get_attribute('value')
    assert textfield == text