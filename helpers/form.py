class form:

    def __init__(self, app):
        self.app = app

    def open_form(self):
        url = 'https://webtrader.roboforex.com/'
        self.app.open_form(url)

    def open_registration_form(self):
        driver = self.app.driver
        driver.find_element_by_class_name("button button_type_quick-demo").click()

    def fill_registration_form(self, registration_data, is18 = False, isConfirm = False):
        driver = self.app.driver
        driver.find_element_by_class_name("input__field input__field_mode_email").send_keys(registration_data.email)
        driver.find_element_by_xpath("//div[@class= \"quick-demo-acc-form__name\"]/input").send_keys(
            registration_data.firstName)
        driver.find_element_by_xpath("//div[@class= \"quick-demo-acc-form__surname\"]/input").send_keys(
            registration_data.lastName)
        driver.find_element_by_class_name("//div[@class= \"quick-demo-acc-form__phone\"]/input").send_keys(
            registration_data.phoneNumber)
        driver.find_element_by_xpath("//div[@class=\'quick-demo-acc-form__country\']//div[@value =" +
                                     registration_data.phoneNumberCountry + "']").click()
        if is18 == False:
            driver.find_element_by_class_name("quick-demo-acc-form__atleast18").click()

        if isConfirm == False:
            driver.find_element_by_class_name("quick-demo-acc-form__termsofuse").click()

    def open_account(self):
        driver = self.app.driver
        driver.find_element_by_class_name("button button_type_brand").click()

    def fill_login_form(self, login_data):
        driver = self.app.driver
        driver.find_element_by_class_name("input__field input__field_mode_email").send_keys(
            login_data.email)
        driver.find_element_by_class_name("password__field password__field_mode_password").send_keys(
            login_data.email).send_keys(
            login_data.password)

    def push_login(self):
        driver = self.app.driver
        driver.find_element_by_class_name("authentication-form__button").click()













