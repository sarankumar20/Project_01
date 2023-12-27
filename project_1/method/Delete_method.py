from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from project_1.locator.locator_delete import Trash_Id

# create class and methods for delete_process
class Delete_id(Trash_Id):
    try:
        def __init__(self, driver):
            self.driver = driver
        # here we enter id_value in other_id box
        def enter_id(self, Id):
            self.driver.find_element(by=By.XPATH, value=self.id_field).send_keys(Id)
        # and we get respective person is visible
        # now we click checkbox
        # and click trash_button
        def click_trash_icon(self):
            self.driver.find_element(by=By.XPATH, value=self.trash_icon).click()
            self.driver.find_element(by=By.XPATH, value=self.delete_alert).click()
        # here after clicking yes button we get successful delete message
        # we capture this message in below method
        def delete_menu_is_displayed(self):
            delete_menu = self.driver.find_element(by=By.XPATH, value=self.success_delete_msg)
            textfy = self.driver.find_element(by=By.XPATH, value=self.msg)
            print(f'after delete person we get {textfy.text}.')
            assert delete_menu.is_displayed

    except NoSuchElementException as exception_1:
        print("no such element")
    except TimeoutException as exception_2:
        print("timeout error")






