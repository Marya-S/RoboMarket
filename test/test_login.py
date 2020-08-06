from model.registration_data import RegistrationData
from model.login_data import LoginData


def test_successful_user_registration(app):
    app.form.open_form()
    app.form.open_registration_form()
    app.form.fill_registration_form(RegistrationData(email="tetsts@mail.ru", firstName="Сергей", lastName="Иванов",
                                                     phoneNumberCountry="Kyrgyzstan: KG +996", phoneNumber=787878))
    app.form.open_account()
    app.assertion.page_is_open()


def test_successful_user_registration_and_login(app):
    app.form.open_form()
    app.form.open_registration_form()
    app.form.fill_registration_form(RegistrationData(email="tetst1s@mail.ru", firstName="Сергей", lastName="Иванов",
                                                     phoneNumberCountry="Kyrgyzstan: KG +996", phoneNumber=787878))
    app.form.open_account()
    app.form.open_form()
#Пароль нужен тот, который ставится после регистрации по дефолту
    app.form.fill_login_form(LoginData(email="tetst1s@mail.ru", password=11111))
    app.assertion.page_is_open()

#Далее нужно создать такие же тесты, но с другими параметрами(с пустыми полями, неверными данными и т.п.) и проверить соответствующиее ошибки
