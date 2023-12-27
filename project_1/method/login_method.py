from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from project_1.locator.locator_login import Element_Home
from project_1.Src.Login_page_data import Value

class Login_element(Element_Home):
    try:
        def __init__(self, driver):
            # instance driver
            self.driver = driver

        def Url_verification(self):
            # here we verify current_url match wit expected_url
            assert self.driver.current_url == Value.homepage_url
            print(f'the current url of the webpage is {self.driver.current_url}')

        def enter_username_field(self, username):
            # if url is match and click,clear,enter a value to username_field
            if self.driver.current_url == Value.homepage_url:
                self.driver.find_element(by=By.NAME, value=self.username_Name).click()
                self.driver.find_element(by=By.NAME, value=self.username_Name).clear()
                self.driver.find_element(by=By.NAME, value=self.username_Name).send_keys(username)
            else:
                print("invalid credit")

        def enter_password_field(self, password):
            # if url is match and click,clear,enter a value to username_field
            if self.driver.current_url == Value.homepage_url:
                self.driver.find_element(By.NAME, value=self.password_Name).click()
                self.driver.find_element(By.NAME, value=self.password_Name).clear()
                self.driver.find_element(By.NAME, value=self.password_Name).send_keys(password)
            else:
                self.driver.close()

        def click_login_button(self):
            # after enter value to username and password_field
            # to click login_button
            self.driver.find_element(By.XPATH, value=self.login_button_xpath).click()

        def warning_message(self):
            # if invalid_login means we want get invalid_creditional message
            msg = self.driver.find_element(by=By.XPATH, value=self.war_msg)
            print(f" this the warning message {msg.text}.")
            expected_invalid = "Invalid credentials"
            assert msg.text.__contains__(expected_invalid)

    except NoSuchElementException as exception_1:
        print("no such element")
    except TimeoutException as exception_2:
        print("timeout error")
