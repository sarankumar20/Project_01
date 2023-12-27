# PIM page
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from project_1.locator.locator_add_employee import Element

# create class and methods for Pim_page
class Employee_Page(Element):
    try:
        def __init__(self, driver):
            self.driver= driver

        def select_pim_menu(self):
            # after enter into dashboard_page we want to navigate Pim_page
            # so locate search_menu and enter pim as key
            self.driver.find_element(by=By.XPATH, value=self.search_menu_locator).send_keys("PIM")
            # after it i click pim_menu
            self.driver.find_element(by=By.XPATH, value=self.pim_menu_locator).click()
            # here, asserting pim_page_url is match with current_url
            expected_pim_url = "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList"
            print(self.driver.current_url)
            assert self.driver.current_url.__eq__(expected_pim_url)

        def select_add_employee_button(self):
            # after we click add_employee button
            self.driver.find_element(by=By.LINK_TEXT, value=self.add_employ_locator).click()
            expected_add_emlp_url = "https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee"
            print(self.driver.current_url)
            # here, asserting add_employee_page_url is match with current_url
            assert self.driver.current_url.__eq__(expected_add_emlp_url)

        # in that add_employee_page
        # we have name,id and save button elements
        # in this method, we are passing value to firstname,middel_name,lastname

        def first_name_input_text_field(self, enter_firstname):
            self.driver.find_element(by=By.NAME, value=self.first_name_locator).click()
            self.driver.find_element(by=By.NAME, value=self.first_name_locator).clear()
            self.driver.find_element(by=By.NAME, value=self.first_name_locator).send_keys(enter_firstname)

        def middel_name_input_text_field(self, enter_middel_name):
            self.driver.find_element(by=By.NAME, value=self.middel_name_locator).click()
            self.driver.find_element(by=By.NAME, value=self.middel_name_locator).clear()
            self.driver.find_element(by=By.NAME, value=self.middel_name_locator).send_keys(enter_middel_name)

        def last_name_input_text_field(self, enter_lastname):
            self.driver.find_element(by=By.NAME, value=self.last_name_locator).click()
            self.driver.find_element(by=By.NAME, value=self.last_name_locator).clear()
            self.driver.find_element(by=By.NAME, value=self.last_name_locator).send_keys(enter_lastname)

        # click save button
        def save_button(self):
            self.driver.find_element(by=By.XPATH, value=self.save_button_locator).click()

        # after saving we want capture success message
        def validate_success_menu_is_displayed(self):
            success=self.driver.find_element(By.XPATH, value=self.success_menu)
            assert success.is_displayed
            success_text = self.driver.find_element(by=By.XPATH, value=self.success_menu_text).text
            print(f'this message after add_employee {success_text}.')
            expected_text="Successfully Saved"
            assert success_text.__eq__(expected_text)

    except NoSuchElementException as exception_1:
        print("no such element")
    except TimeoutException as exception_2:
        print("timeout error")












