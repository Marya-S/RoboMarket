class assertion:
    def __init__(self, app):
        self.app = app

    def page_is_open(self):
        driver = self.app.driver
        assert ("Demo Account details") == driver.find_element_by_id("modal-window__title").text