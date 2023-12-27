from project_1.method.login_method import Login_element
from project_1.Src.Login_page_data import Value

# combine all methods in single method by pom module

class Invalid_login(Value):

    def __init__(self, driver):
        self.driver = driver

    def invalid_creditional(self):
        # first we, get login details from Home_page class and signin
        home_page = Login_element(self.driver)
        # here validating url of the page
        home_page.Url_verification()
        # here passing valid_username to username_field
        home_page.enter_username_field(self.username_1)
        # here passing valid_password to password_field
        home_page.enter_password_field(self.password_2)
        # click login button
        home_page.click_login_button()
        # if login is not success we capture warning message
        home_page.warning_message()
        assert self.driver.titlt == 'orangerm'
