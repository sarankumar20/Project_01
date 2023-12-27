from project_1.method.Employee_Edit_method import Search_by_name
from project_1.method.PIM_Page_method import Employee_Page
from project_1.method.personal_page_method import Personal_page
from project_1.pom.valid_login import Signin
from project_1.Src.edit_data import Edit_datas

# combine all methods in single method by pom module

class Edit_Id(Signin, Edit_datas):

    def __init__(self, driver):
        super().__init__(driver)

    def edit_detail(self):
        # calling Login class form validate_login_function
        # to signin
        self.valid_username_and_valid_password()
        # navigate to dashboard page
        # calling employee_page class from pim_page file
        pim_page = Employee_Page(self.driver)
        # search_menu in that passing pim value
        # and select pim menu in down of it
        pim_page.select_pim_menu()
        # calling  search_by_name class from employee_edit file
        edit_details = Search_by_name(self.driver)
        # verify current_url and expected_url in it
        edit_details.verify_page_url()
        # in name_field passing 'saran' value
        edit_details.search_with_name(self.name)
        # click search button
        edit_details.click_search_button()
        # after search_it we get respective detail in bottom and click check box
        edit_details.click_check_box()
        # and click edit icon in it
        edit_details.click_edit_icon()
        # navigate to personal page
        detail = Personal_page(self.driver)
        detail.verify_personal_details_page()
        # edit nickname with 'kumar'
        detail.add_nickname(self.nick)
        # edit other_id with '7098'
        detail.entering_other_id(self.OID)
        # click save button and print success message
        detail.click_save_button()
        # to logout
        self.click_logout_button()