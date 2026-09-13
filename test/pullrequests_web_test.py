import allure
import pytest
from .steps import web_steps as steps
from .marks import microservice, layer, owner, tm4j, jira_issues
from .steps.web_steps import close_pull_request_for_branch

pytestmark = [
    layer("web"),
    owner("eroshenkoam"),
    allure.feature("Pull Requests")
]

OWNER = "allure-framework"
REPO = "allure2"
BRANCH = "new-feature"


@pytest.fixture(scope="module")
def web_driver():
    steps.start_driver()
    yield
    steps.stop_driver()


@microservice("Billing")
@allure.story("Create new pull request")
@pytest.mark.web
@pytest.mark.regress
@pytest.mark.smoke
@jira_issues("AE-3")
@allure.title("Creating new issue for authorized user")
def test_should_create_pull_request(web_driver):
    steps.open_pull_requests_page(OWNER, REPO)
    steps.create_pull_request_from_branch(BRANCH)
    steps.should_see_pull_request_for_branch(BRANCH)


@microservice("Repository")
@allure.story("Close existing pull request")
@pytest.mark.web
@pytest.mark.regress
@jira_issues("AE-4")
@allure.title("Deleting existing issue for authorized user")
def test_should_close_pull_request(web_driver):
    steps.open_pull_requests_page(OWNER, REPO)
    steps.create_pull_request_from_branch(BRANCH)
    close_pull_request_for_branch(BRANCH)
    steps.should_see_pull_request_for_branch(BRANCH)
