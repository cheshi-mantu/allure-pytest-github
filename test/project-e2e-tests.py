import allure
import pytest
from .steps import web_steps as steps
from .marks import layer, owner


pytestmark = [
    layer("none"),
    owner("egorivanov"),
]

def test_should_project():
    