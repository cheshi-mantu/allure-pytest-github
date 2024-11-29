from .marks import layer, owner
import allure
import pytest
import time
from .marks import microservice, layer, owner, tm4j, jira_issues


pytestmark = [
    layer("e2e"),
    owner("egorivanov"),
    allure.feature("Project")
]


@pytest.fixture(scope="module")
def login():
    """Fixture for logging in to the application."""
    with allure.step("Open log-in page"):
        allure.attach("Open page:", "https://demo.testops.cloud", allure.attachment_type.TEXT)
    with allure.step("Click log-in button"):
        pass
    with allure.step("Enter credentials"):
        with allure.step("Enter valid email"):
            time.sleep(0.404)  # Simulating delay
            allure.attach("email:", "valid@email.com", allure.attachment_type.TEXT)
        with allure.step("Enter valid password"):
            time.sleep(0.500)  # Simulating delay
            allure.attach("password:", "validP@ssword", allure.attachment_type.TEXT)
        with allure.step("Click OK"):
            pass
    with allure.step("Check log-in is successful"):
        time.sleep(0.945)  # Simulating delay
        with allure.step("User's avatar must be visible in the side menu"):
            with allure.step("Check <div> related to user menu is visible"):
                pass
    return True  # Simulating successful login

@allure.story("Creation of a project")
@allure.title("Successful creation of a project by authenticated user")
@allure.description("Successful creation of a project by authenticated user")
@jira_issues("AE-12")
@jira_issues("AE-22")
@pytest.mark.web
@pytest.mark.critical
def test_create_project(login):
    """Test for creating a new project."""
    with allure.step("Checking the creation of a new project"):
        with allure.step("Click `Create new project`"):
            time.sleep(1.234)  # Simulating delay
        with allure.step("Enter New Project name"):
            pass
        with allure.step("Enter the description"):
            pass
        with allure.step("Click Submit"):
            time.sleep(2.134)  # Simulating delay
        with allure.step("Assert"):
            time.sleep(0.945)  # Simulating delay
            with allure.step("User is redirected to new project"):
                pass
            with allure.step("User sees the empty list of test cases"):
                pass