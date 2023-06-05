import allure
import pytest
from .steps import rest_steps as steps
from .marks import microservice, layer, owner, tm4j, jira_issues

@allure.id("187698")
@allure.title("Successful auth with username and password")
@allure.tag("critical", "regress", "smoke")
@allure.story("Built-in auth")
@allure.feature("Authentication")
@allure.label("msrv", "UAA")
@allure.label("owner", "egorivanov")
def test_should_authenticate_user_with_email():
    with allure.step("Open main page"):
        pass
    with allure.step("Enter the creds"):
        with allure.step("username"):
            pass
    with allure.step("passwrod"):
        pass
    with allure.step("Click login"):
        pass
    with allure.step("Login is successful"):
        with allure.step("Avatar is present"):
            pass
