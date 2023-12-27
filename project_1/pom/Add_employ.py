from project_1.Src.personal_data import Details
from project_1.method.PIM_Page_method import Employee_Page
from project_1.method.personal_page_method import Personal_page
from project_1.pom.valid_login import Signin

# combine all methods in single method by pom module

class Profile(Signin, Details):

    def __init__(self, driver):
        super().__init__(driver)

    def profile_creation(self):
        # calling Login class form validate_login_function
        # to signin
        self.valid_username_and_valid_password()
        # navigate to dashboard page
        # calling employee_page class from pim_page file
        pim_page = Employee_Page(self.driver)
        # search_menu in that passing pim value
        # and select pim menu in down of it
        pim_page.select_pim_menu()
        # verify the page with header_text because this page url is dynamic changing
        # after verified click the add_menu option in the page
        pim_page.select_add_employee_button()
        # passing firstname value as 'sarvan'
        pim_page.first_name_input_text_field(self.first_name)
        # passing middel name as 'kumar'
        pim_page.middel_name_input_text_field(self.middel_name)
        # passing last name as 'ravi'
        pim_page.last_name_input_text_field(self.last_name)
        # and click save button
        # if its successful saved we capture save successful message and print it
        pim_page.save_button()
        # after that navigate to personal_details page and
        # calling personal_page class from personal_detail_page file
        detail = Personal_page(self.driver)
        # verify it by header_text 'Personal_Details'
        detail.verify_personal_details_page()
        # for values calling details class from file
        # here passing valid nickname 'sk'
        detail.add_nickname(self.nick_name)
        # here passing valid other_id '4079'
        detail.entering_other_id(self.other_id)
        # here passing valid license_no '345DsAjk543'
        detail.entering_license(self.license_no)
        # here passing  license_expiry_date "2015-01-30"
        detail.entering_license_expiry(self.license_ex_date)
        # here passing  ssn 'nil'
        detail.entering_ssn(self.ssn_value)
        # here passing  sin 'nil'
        detail.entering_sin(self.sin_value)
        # click nationality with 'Indian' value
        detail.click_nationality()
        # click martial_status with 'Single' value
        detail.click_martial_status()
        # here passing DOB "2001-21-02"
        detail.enter_date_birth(self.DOB)
        # click male option in radiobutton
        detail.click_male_radio_button()
        # passing 'no' value to military field
        detail.entering_military_field(self.military_value)
        # click smoker_checkbox
        detail.clicking_smoker_check_box()
        # click save button and print success message
        detail.click_save_button()
        # click logout
        self.click_logout_button()
