from project_1.method.login_method import Login_element
from project_1.method.dashboard_method import dashboard_page
from project_1.Src.Login_page_data import Value

class Signin(Value):

    def __init__(self, driver):
        self.driver = driver

    # first we, get login details from Home_page class and signin
    def valid_username_and_valid_password(self):
        home_page = Login_element(self.driver)
        # here validating url of the page
        home_page.Url_verification()
        # here passing valid_username to username_field
        home_page.enter_username_field(self.username_1)
        # here passing valid_password to password_field
        home_page.enter_password_field(self.password_1)
        # click login button
        home_page.click_login_button()

    # after successful signin ,navigate to dashboard page
    def verify_dashboard_page(self):
        # get dashboard details from Dashboard_menu class
        # here validating url of the page
        dashboard = dashboard_page(self.driver)
        dashboard.verify_dashboard_page()

    def click_logout_button(self):
        dashboard = dashboard_page(self.driver)
        # click profile tab and in dropdown click logout button
        dashboard.click_logout_button()
        # re-verifying after logout again came to homepage or not
        home_page = Login_element(self.driver)
        # if it came to homepage it prints homepage url
        home_page.Url_verification()