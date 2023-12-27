# employee_edit_page
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from project_1.locator.locator_employee import Element_information
from project_1.Src.edit_data import Edit_datas

# create class and methods for Employee_edit_page

class Search_by_name(Element_information, Edit_datas):
    try:
        def __init__(self, driver):
            self.driver = driver
        def verify_page_url(self):
            # we are importing expected_url from Data_package
            assert self.driver.current_url.__eq__(self.eml_url)
        def search_with_name(self, enter_name):
            self.driver.find_element(by=By.XPATH, value=self.name_field).send_keys(enter_name)
        def click_search_button(self):
            self.driver.find_element(by=By.XPATH, value=self.search_button).click()
        def click_check_box(self):
            self.driver.find_element(by=By.XPATH, value=self.check_box).click()
        def click_edit_icon(self):
            self.driver.find_element(by=By.XPATH, value=self.edit_button).click()

    except NoSuchElementException as exception_1:
        print("no such element")
    except TimeoutException as exception_2:
        print("timeout error")








