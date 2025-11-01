from selene import browser, be
import pytest


@pytest.fixture(params=['Desktop', 'Mobile'])
def browser_size_window(request):
    if request.param == 'Desktop':
        browser.config.window_width = 1920
        browser.config.window_height = 1080
    elif request.param == 'Mobile':
        browser.config.window_width = 455
        browser.config.window_height = 866


@pytest.mark.parametrize('browser_size_window', ['Desktop'], indirect=True)
def test_github_desktop(browser_size_window):
    browser.open("https://github.com/")
    browser.element(".HeaderMenu-link--sign-up").should(be.visible).click()
    assert browser.element('.//h2[contains(text(), "Sign up for GitHub")]').should(be.visible)


@pytest.mark.parametrize('browser_size_window', ['Mobile'], indirect=True)
def test_github_mobile(browser_size_window):
    browser.open("https://github.com/com")
    browser.element(".Button-label").click()
    browser.element(".HeaderMenu-link--sign-up").should(be.visible).click()
    assert browser.element('.//h2[contains(text(), "Sign up for GitHub")]').should(be.visible)
