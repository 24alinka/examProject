from constants.contact_us_page import ContactUsConstants
from pages.utils import log_decorator
from pages.base_page import BasePage


class ContactUsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.constants = ContactUsConstants()

    @log_decorator
    def create_message(self, contact):
        """Create post using provided values"""
        self.fill_field(xpath=self.constants.CONTACT_FULL_NAME_INPUT_XPATH, value=contact.name)
        self.fill_field(xpath=self.constants.CONTACT_EMAIL_INPUT_XPATH, value=contact.email)
        self.fill_field(xpath=self.constants.CONTACT_TEXT_AREA_XPATH, value=contact.message)
        self.click(xpath=self.constants.CONTACT_SUBMIT_BUTTON_XPATH)

    @log_decorator
    def verify_successfully_sent_message(self):
        """Create post using provided values"""
        assert self.get_element_text(
            self.constants.CONTACT_RESULT_AFTER_SENT_MESSAGE_XPATH) \
               == self.constants.CONTACT_RESULT_AFTER_SENT_MESSAGE_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.CONTACT_RESULT_AFTER_SENT_MESSAGE_XPATH)}"
