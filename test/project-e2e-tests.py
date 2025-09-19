import allure
import pytest
from .steps import web_steps as steps
from .marks import layer, owner

pytestmark = [
    layer("api"),
    owner("bugsbunny"),
]

def test_should_project():
    with allure.step("Preconditions"):
        with allure.step(
                "Given a user is logged in\n"
                "When they navigate to the dashboard\n"
                "Then they should see their account details"
        ):
            pass
    with allure.step(""):
        print("then some actions")
        pass