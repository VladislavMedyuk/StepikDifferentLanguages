import time

from selenium.webdriver.common.by import By

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/."

class TestLanguages:
    def test_button_add_to_basket_is_visible(self, browser):
        browser.get(link)
        time.sleep(10)

        assert browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket"), "There isn't busket button on this page"