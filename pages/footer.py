from constants.contact_us_page import ContactUsConstants
from pages.base_page import BasePage
from constants.footer import FooterConstants

from pages.utils import log_decorator


class Footer(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.constants = FooterConstants()
        self.contact_us_page = ContactUsConstants()

    @log_decorator
    def navigate_to_contact_page(self):
        """Click on Contact Us button"""
        self.click(self.constants.FOOTER_CONTACT_US_BUTTON_XPATH)