import pytest
from selene.support.shared import browser
from selene import be, have

@pytest.fixture
def set_window_size():
    browser.config.window_height = 800
    browser.config.window_width = 600


def test_search_works(set_window_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_not_works(set_window_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('ehgieruhgeiurhgierg').press_enter()
    browser.element('.card-section').should(have.text('По запросу ehgieruhgeiurhgierg ничего не найдено.'))
