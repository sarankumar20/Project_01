
# locators for delete_elements
class Trash_Id:
    id_field = '(//input[@class="oxd-input oxd-input--active"])[2]'
    trash_icon = '//button[contains(@class,"oxd-icon-button")]/i[@class="oxd-icon bi-trash"]'
    delete_alert = '//button[text()=" Yes, Delete "]'
    success_delete_msg = '//div[@id="oxd-toaster_1"]'
    msg = '//div[@id="oxd-toaster_1"]/div/div/div[2]/p[2]'