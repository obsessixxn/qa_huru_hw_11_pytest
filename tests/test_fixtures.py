import pytest
from selene import browser, be


@pytest.fixture()
def setup_mobile():
    browser.config.window_width = 455
    browser.config.window_height = 855


@pytest.fixture()
def setup_desktop():
    browser.config.window_width = 1920
    browser.config.window_height = 1080


def test_github_fixture_desktop(setup_desktop):
    browser.open('https://github.com')
    browser.element(".HeaderMenu-link--sign-up").should(be.visible).click()
    assert browser.element('.//h2[contains(text(), "Sign up for GitHub")]').should(be.visible)


def test_github_fixture_mobile(setup_mobile):
    browser.open("https://github.com/com")
    browser.element(".Button-label").click()
    browser.element(".HeaderMenu-link--sign-up").should(be.visible).click()
    assert browser.element('.//h2[contains(text(), "Sign up for GitHub")]').should(be.visible)
