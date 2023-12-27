from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from project_1.locator.locator_dashboard import Elements

class dashboard_page(Elements):
    try:
        # constructor
        def __init__(self, driver):
            self.driver = driver

        # method
        def verify_dashboard_page(self):
            # after login successful we get into dashboard page
            # I am verified header with expected text
            head_tag = self.driver.find_element(by=By.XPATH, value=self.dashboard_text).text
            print(head_tag)
            # I am asserting actual_page_url is equal to  expected url
            expected_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'
            assert self.driver.current_url.__contains__(expected_url)

        def click_logout_button(self):
            # after i want to log out by clicking profile_dropdown_menu
            self.driver.find_element(by=By.CLASS_NAME, value=self.user_profile_dropdown_menu).click()
            # click logout_menu
            self.driver.find_element(by=By.LINK_TEXT, value=self.logout_button).click()

    except NoSuchElementException as exception_1:
        print("no such element")
    except TimeoutException as exception_2:
        print("timeout error")