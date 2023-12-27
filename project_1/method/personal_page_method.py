# personal_detail_methods
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from project_1.locator.locator_personal import Element_Personal

# create class and methods for personal_details
# here we are passing respective locators to the methods
class Personal_page(Element_Personal):
    try:
        def __init__(self, driver):
            self.driver = driver
        def verify_personal_details_page(self):
            # we assert header of the page
            # note:in this page we have dynamic url, so we didn't assert it
            expected_header_text = "Personal Details"
            actual_header = self.driver.find_element(by=By.XPATH, value=self.head_tag_locator).text
            assert actual_header.__eq__(expected_header_text)
            # print it
            header = self.driver.find_element(by=By.XPATH, value=self.head_tag_locator).text
            print(header)
        def add_nickname(self, name):
            self.driver.find_element(by=By.XPATH, value=self.nickname_locator).click()
            self.driver.find_element(by=By.XPATH, value=self.nickname_locator).clear()
            self.driver.find_element(by=By.XPATH, value=self.nickname_locator).send_keys(name)
        def entering_other_id(self, id_no):
            self.driver.find_element(by=By.XPATH, value=self.other_id_locator).click()
            self.driver.find_element(by=By.XPATH, value=self.other_id_locator).clear()
            self.driver.find_element(by=By.XPATH, value=self.other_id_locator).send_keys(id_no)
        def entering_license(self, license_no):
            self.driver.find_element(by=By.XPATH, value=self.driving_license).click()
            self.driver.find_element(by=By.XPATH, value=self.driving_license).clear()
            self.driver.find_element(by=By.XPATH, value=self.driving_license).send_keys(license_no)
        def entering_license_expiry(self, expiry_date):
            self.driver.find_element(by=By.XPATH, value=self.license_expiry_locator).click()
            self.driver.find_element(by=By.XPATH, value=self.license_expiry_locator).send_keys(expiry_date)
        def entering_ssn(self, ssn_no):
            self.driver.find_element(by=By.XPATH, value=self.ssn_locator).click()
            self.driver.find_element(by=By.XPATH, value=self.ssn_locator).send_keys(ssn_no)
        def entering_sin(self, sin_no):
            self.driver.find_element(by=By.XPATH, value=self.sin_locator).click()
            self.driver.find_element(by=By.XPATH, value=self.sin_locator).send_keys(sin_no)
        def click_nationality(self):
            self.driver.find_element(by=By.XPATH, value=self.nationality_locator).click()
            self.driver.find_element(by=By.XPATH, value=self.indian_value).click()
        def click_martial_status(self):
            self.driver.find_element(by=By.XPATH, value=self.martial_locator).click()
            self.driver.find_element(by=By.XPATH, value=self.single_value).click()
        def enter_date_birth(self, dob):
            self.driver.find_element(by=By.XPATH, value=self.DOB).send_keys(dob)
        def click_male_radio_button(self):
            male = self.driver.find_element(by=By.XPATH, value=self.radio_butt_Male)
            if male.is_selected():
                print("is selected")
            else:
                male.click()
        def entering_military_field(self, value):
            self.driver.find_element(by=By.XPATH, value=self.Military).send_keys(value)
        def clicking_smoker_check_box(self):
            self.driver.find_element(by=By.XPATH, value=self.smoker).click()
        def click_save_button(self):
            self.driver.find_element(by=By.XPATH, value=self.save_it).click()

    except NoSuchElementException as exception_1:
        print("no such element")
    except TimeoutException as exception_2:
        print("timeout error")




