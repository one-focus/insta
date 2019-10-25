import time

from behave import *

from features.pages.login_page import LoginPage


@given("open login page")
def step_impl(context):
    context.driver.get("https://www.instagram.com/accounts/login/")


@when('I type "{username}" in username field')
def step_impl(context, username):
    login_page = LoginPage(context.driver)
    login_page.enter_username(username)


@when('I type "{password}" in password field')
def step_impl(context, password):
    login_page = LoginPage(context.driver)
    login_page.enter_password(password)


@when("I click login button")
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.click_login()
    time.sleep(5)


@given("I login")
def step_impl(context):
    context.driver.get("https://www.instagram.com/accounts/login/")
    login_page = LoginPage(context.driver)
    login_page.enter_username(context.config.get("settings", "username"))
    login_page.enter_password(context.config.get("settings", "password"))
    login_page.click_login()
    time.sleep(5)


@then("I see validation message for")
def step_impl(context):
    for row in context.table:
        username = row["username"]
        password = row["password"],
        text = row["message"]
        context.execute_steps('''
    When I type "{username}" in username field
    When I type "{password}" in password field
    When I click element with text "Log In"
    Then I see element with text "{text}"
        '''.format(username=row["username"], password=row["password"], text=row["message"]))
        time.sleep(2)
