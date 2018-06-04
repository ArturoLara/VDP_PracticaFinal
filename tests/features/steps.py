from lettuce import step
from lettuce import world
import pdb

@step('I have the text "(.*)"')
def have_the_text(step, text):
    world.text = text


@step('I put it in the textfield')
def put_text_click_e_bottom(step):
    world.driver.find_element_by_id("id_text").send_keys(world.text)

@step('I see that text in the result text')
def check_result_text(step):
    result_text = world.driver.find_element_by_id("answer").text
    assert result_text == step.multiline


@step('I click the execute button')
def click_execute_button(step):
    world.driver.find_element_by_id("execute").click()


@step('I click the reset bottom')
def click_r_buttom(step):
    world.driver.find_element_by_id("reset").click()


@step('I have in the textfield the text "(.*)"')
def put_text_at_textfield(step, text):
    world.driver.find_element_by_id("id_text").send_keys(text)


@step('I see in the textfield the text "(.*)"')
def check_text(step, text):
    textfield = world.driver.find_element_by_id("id_text").get_attribute('value')
    assert textfield == text
