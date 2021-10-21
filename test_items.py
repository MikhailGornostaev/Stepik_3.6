import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_add_to_basket_button(browser):
    browser.get(link)
    # time.sleep(30)
    button = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    button_test = len(button)
    assert button_test == 1, "Pustota! :("

