from lettuce import step
from lettuce import world

@step('I have the text "(.*)"')
def have_the_text(step, text):
    world.text = text


@step('I put it in the url textfield')
def put_text_click_e_bottom(step):
    world.driver.find_element_by_id("id_text").send_keys(world.text)
    print("1")

@step('I put it in the date textfield')
def put_text_click_e_bottom(step):
    world.driver.find_element_by_id("id_date").send_keys(world.text)
    print("1")


@step('I see that text in the result text')
def check_result_text(step):
    result_text = world.driver.find_element_by_id("answer").text
    assert result_text == step.multiline
    print("1")


@step('I click the seeDate button')
def click_execute_button(step):
    world.driver.find_element_by_id("executeDate").click()
    print("1")

@step('I click the execute button')
def click_execute_button(step):
    world.driver.find_element_by_id("execute").click()
    print("1")


@step('I see in the url textfield the text "(.*)"')
def check_text(step, text):
    textfield = world.driver.find_element_by_id("id_text").get_attribute('value')
    assert textfield == text
    print("1")

@step('I see in the date textfield the text "(.*)"')
def check_text(step, text):
    textfield = world.driver.find_element_by_id("id_date").get_attribute('value')
    assert textfield == text
    print("1")
