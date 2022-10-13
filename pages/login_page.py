from pages.utils import log_decorator
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        from constants.login_page import LoginPageConstants
        self.constants = LoginPageConstants()
        from pages.header import Header
        self.header = Header(self.driver)

    @log_decorator
    def login_form(self, email, password):
        """Login provided values"""
        self.fill_field(xpath=self.constants.LOGIN_EMAIL_INPUT_XPATH, value=email)
        self.fill_field(xpath=self.constants.LOGIN_PASSWORD_INPUT_XPATH, value=password)
        self.click(xpath=self.constants.LOGIN_CHECKBOX_XPATH)
        self.click(xpath=self.constants.LOGIN_CONFIRM_BUTTON_XPATH)

    @log_decorator
    def email_for_forgot_password(self, email):
        """Enter password recovery email."""
        self.fill_field(xpath=self.constants.LOGIN_EMAIL_FORGOT_XPATH, value=email + Keys.ENTER)

    @log_decorator
    def verify_log_in_error(self):
        """Verify log in error message"""
        assert self.get_element_text(
            self.constants.LOGIN_ERROR_MESSAGE_XPATH) == self.constants.LOGIN_ERROR_MESSAGE_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.LOGIN_ERROR_MESSAGE_XPATH)}"

    @log_decorator
    def click_forgot_button(self):
        """Click on the forgot button"""
        self.click(xpath=self.constants.LOGIN_FORGOT_PASSWORD_XPATH)

    @log_decorator
    def click_on_recover_button(self):
        """Click on the recover button"""
        self.click(xpath=self.constants.LOGIN_RECOVER_BUTTON_XPATH)

    @log_decorator
    def verify_sent_email(self):
        """Verify sent message"""
        assert self.get_element_text(
            self.constants.LOGIN_SENT_YOU_XPATH) == self.constants.LOGIN_SENT_YOU_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.LOGIN_SENT_YOU_XPATH)}"