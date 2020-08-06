from selenium import webdriver
from helpers.form import form
from helpers.session import SessionHelper
from helpers.assertion import assertion


class Application:

    def __init__(self, browser):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.form = form(self)
        self.session = SessionHelper(self)

    def open_start_page(self, base_url):
        wd = self.wd
        wd.get(base_url)

    def destroy(self):
        self.wd.quit()

