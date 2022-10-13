from constants.start_page import StartPageConstants
from pages.base_page import BasePage
from pages.contact_us_page import ContactUsPage
from pages.footer import Footer
from pages.login_page import LoginPage
from pages.register_page import RegisteredPage
from pages.utils import wait_until_ok, log_decorator
from pages.header import Header


class StartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConstants()
        self.header = Header(self.driver)
        self.login_page = LoginPage(self.driver)
        self.register_page = RegisteredPage(self.driver)
        self.footer = Footer(self.driver)
        self.contact_us_page = ContactUsPage(self.driver)

    @log_decorator
    def subscribe(self, email):
        """Subscribe in as the user"""
        from time import sleep
        sleep(1)
        # Fill email
        self.fill_field(xpath=self.constants.INPUT_NEWSLETTER_XPATH, value=email)
        self.click(xpath=self.constants.SUBSCRIBE_BUTTON_FOR_EMAIL_XPATH)

    @log_decorator
    def click_on_subscribe_button(self):
        """Click on the subscribe button"""
        self.click(xpath=self.constants.SUBSCRIBE_BUTTON_FOR_EMAIL_XPATH)

    @log_decorator
    def verify_subscribe(self):
        """Verify subscribe in as the user"""
        from time import sleep
        sleep(1)
        assert self.get_element_text(
            self.constants.THANK_YOU_TEXT_XPATH) == self.constants.THANK_YOU_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.THANK_YOU_TEXT_XPATH)}"

    @log_decorator
    def verify_error_message(self):
        """Verify error subscribe in as the user"""
        from time import sleep
        sleep(1)
        assert self.get_element_text(
            self.constants.ERROR_SUBSCRIBE_XPATH) == self.constants.ERROR_SUBSCRIBE_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.ERROR_SUBSCRIBE_XPATH)}"

    @log_decorator
    def click_on_the_product_and_add_to_the_shopping_cart(self):
        """Click on the product"""
        self.click(xpath=self.constants.OPEN_PRODUCT_XPATH)
        self.click(xpath=self.constants.ADD_PRODUCT_TO_THE_SHOPPING_CART_XPATH)

    @log_decorator
    def verify_added_product_to_the_shopping_cart(self):
        """Verify added product to the shopping cart"""
        from time import sleep
        sleep(1)
        assert self.get_element_text(
            self.constants.POP_UP_ADDED_PRODUCT_TO_THE_SHOPPING_CART_XPATH) \
               == self.constants.POP_UP_ADDED_PRODUCT_TO_THE_SHOPPING_CART_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.POP_UP_ADDED_PRODUCT_TO_THE_SHOPPING_CART_XPATH)}"