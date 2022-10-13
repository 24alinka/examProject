from pages.utils import log_decorator
from pages.base_page import BasePage


class RegisteredPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        from constants.register_page import RegisterPageConstants
        self.constants = RegisterPageConstants()
        from pages.header import Header
        self.header = Header(self.driver)

    @log_decorator
    def register_form(self, user):
        """Sign up as the user"""
        # Fill data
        self.fill_field(xpath=self.constants.REGISTER_INPUT_FIRST_NAME_XPATH, value=user.firstname)
        self.fill_field(xpath=self.constants.REGISTER_INPUT_LAST_NAME_XPATH, value=user.lastname)
        self.fill_field(xpath=self.constants.REGISTER_INPUT_EMAIL_XPATH, value=user.email)
        self.fill_field(xpath=self.constants.REGISTER_INPUT_PASSWORD_XPATH, value=user.password)
        self.fill_field(xpath=self.constants.REGISTER_INPUT_CONFIRM_PASSWORD_XPATH, value=user.password)
        # Click button
        self.click(xpath=self.constants.REGISTER_BUTTON_XPATH)

    def verify_successful_registration(self):
        """Verify successful registration"""
        assert self.get_element_text(
            self.constants.REGISTER_SUCCESSFULLY_REGISTRATION_XPATH) == \
               self.constants.REGISTER_SUCCESSFULLY_REGISTRATION_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.REGISTER_SUCCESSFULLY_REGISTRATION_XPATH)}"

    def verify_wrong_email(self):
        """Verify wrong email message"""
        assert self.get_element_text(
            self.constants.ERROR_REGISTER_WRONG_EMAIL) == self.constants.ERROR_REGISTER_WRONG_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.ERROR_REGISTER_WRONG_EMAIL)}"
