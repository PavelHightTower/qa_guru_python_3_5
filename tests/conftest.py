import pytest
from selene.support.shared import browser


@pytest.fixture(scope="function", autouse=True)
def browser_set():
    browser.config.window_height = 950
    browser.config.window_width = 1600
    browser.config.base_url = "https://demoqa.com/"

    yield

    browser.quit()
