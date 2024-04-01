from pytest_metadata.plugin import metadata_key
from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    global driver
    if browser=='chrome':
        driver=webdriver.Chrome()

    elif browser=='firefox':
        driver=webdriver.Firefox()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


#####################Pytest Html Report######################
def pytest_configure(config):
    config.stash[metadata_key]['project Name']="E-commerces"
    config.stash[metadata_key]['Module Name']="customers"
    config.stash[metadata_key]['Tester']="Sandeep"


@pytest.mark.hookimpl()
def pytest_metadata(metadata):
    metadata.pop("Java_home",None)
    metadata.pop("plugin",None)