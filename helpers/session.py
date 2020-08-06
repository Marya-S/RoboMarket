class SessionHelper:

    def __init__(self, app):
        self.app = app

    def open_browser(self):
        driver = self.app.wd

    def close(self):
        driver = self.app.wd
        driver.quit()