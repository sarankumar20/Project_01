from project_1.method.Delete_method import Delete_id
from project_1.method.Employee_Edit_method import Search_by_name
from project_1.method.PIM_Page_method import Employee_Page
from project_1.pom.valid_login import Signin
from project_1.Src.delete_data import Data
# combine all methods in single method by pom module

class Delete(Signin, Data):

    def __init__(self, driver):
        super().__init__(driver)

    def delete_employee_with_name(self):
        # first we, get login details from Home_page class and signin
        self.valid_username_and_valid_password()
        pim_page = Employee_Page(self.driver)
        pim_page.select_pim_menu()
        edit_details = Search_by_name(self.driver)
        edit_details.verify_page_url()
        edit_details.click_search_button()
        delete = Delete_id(self.driver)
        delete.enter_id(self.id)
        edit_details.click_check_box()
        delete.click_trash_icon()
        delete.delete_menu_is_displayed()
        # to logout
        self.click_logout_button()