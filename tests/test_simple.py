import pytest
from selene import browser, be


@pytest.fixture()
def browser_size_window(width, height):
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


@pytest.mark.parametrize('width, height',
                         [(1920, 1080), (1024, 866), (1440, 962), (1024, 866), (768, 866),
                          (425, 866)])
def test_github_desktop(browser_size_window, width, height):
    if width < 1024:
        pytest.skip('It is for mobile resolution')
    else:
        browser.open('https://github.com')
        browser.element(".HeaderMenu-link--sign-up").should(be.visible).click()
        assert browser.element('.//h2[contains(text(), "Sign up for GitHub")]').should(be.visible)


@pytest.mark.parametrize('width, height',
                         [(1920, 1080), (768, 866), (425, 866), (375, 850), (1024, 768), (1366, 768)])
def test_github_mobile(browser_size_window, width, height):
    if width >= 1024:
        pytest.skip('It is for desktop resolution')
    else:
        browser.open("https://github.com/com")
        browser.element(".Button-label").click()
        browser.element(".HeaderMenu-link--sign-up").should(be.visible).click()
        assert browser.element('.//h2[contains(text(), "Sign up for GitHub")]').should(be.visible)