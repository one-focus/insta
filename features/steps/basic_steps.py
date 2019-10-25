from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@when('I click element with text "{value}"')
def step_impl(context, value):
    element = (By.XPATH, "//*[text() = '{}']".format(value))
    WebDriverWait(context.driver, 10).until(ec.element_to_be_clickable(element), "Unable to click element").click()


@then('I see element with text "{value}"')
def step_impl(context, value):
    element = (By.TAG_NAME, "body")
    WebDriverWait(context.driver, 10).until(ec.text_to_be_present_in_element(element, value), "Unable to find text")