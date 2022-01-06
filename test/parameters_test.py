import allure
import pytest
from .marks import microservice, layer, owner, tm4j, jira_issues

pytestmark = [
    layer("web"),
    owner("egorivanov"),
]

BRAND = ["juniors", "grownups"]
LOCALE = ["de_de", "en_us", "en_uk"]

@allure.title("Checking webpage for a brand with different locale")
@allure.feature("main page welcome screen")
@allure.story("Testing main page welcome screen")
@microservice("welcome")
@pytest.mark.parametrize("brand", BRAND)
@pytest.mark.parametrize("locale", LOCALE)
def test_should_check_page_welcome_screen(brand, locale):
    with allure.step("Open welcome screen" + brand + " with locale " + locale):
        pass
    with allure.step("Check if brand's " + brand + " welcome message is  " + locale):
        pass

