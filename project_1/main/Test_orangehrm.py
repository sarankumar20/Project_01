import pytest
from project_1.pom.invalid_login import Invalid_login
from project_1.pom.valid_login import Signin
from project_1.pom.Add_employ import Profile
from project_1.pom.Edit_employe import Edit_Id
from project_1.pom.delete_by_id import Delete
class Test_Functionalities:

    @pytest.mark.usefixtures("browser_setup_and_teardown")
    def test_TC_1_Login_with_valid_creditional(self):
        Data_1 = Signin(self.driver)
        Data_1.valid_username_and_valid_password()
        Data_1.verify_dashboard_page()
        Data_1.click_logout_button()

    @pytest.mark.usefixtures("browser_setup_and_teardown")
    def test_TC_2_Login_with_invalid_creditional(self):
        Data_2 = Invalid_login(self.driver)
        Data_2.invalid_creditional()

    @pytest.mark.usefixtures("browser_setup_and_teardown")
    def test_tc_1_add_employee(self):
        create_profile = Profile(self.driver)
        create_profile.profile_creation()

    @pytest.mark.usefixtures("browser_setup_and_teardown")
    def test_tc_2_edit_employee_details(self):
        Data_3 = Edit_Id(self.driver)
        Data_3.edit_detail()

    @pytest.mark.usefixtures("browser_setup_and_teardown")
    def test_tc_3_delete_created_employee(self):
        Data_4 = Delete(self.driver)
        Data_4.delete_employee_with_name()