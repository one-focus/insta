import configparser

import allure
from selenium import webdriver


def before_all(context):
    context.driver = webdriver.Chrome("C:/Users/a.kardash/Desktop/python_course/chromedriver.exe")
    context.driver.implicitly_wait(5)

    parser = configparser.ConfigParser()
    parser.read("features/behave.ini")
    context.config = parser


def before_scenario(context, scenario):
    context.driver.delete_all_cookies()


def after_step(context, step):
    if step.status == "failed":
        allure.attach(context.driver.get_screenshot_as_png(),
                      name="screenshot",
                      attachment_type=allure.attachment_type.PNG)


def after_all(context):
    context.driver.quit()
