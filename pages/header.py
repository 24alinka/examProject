from constants.header import HeaderConstants
from constants.login_page import LoginPageConstants
from constants.shopping_page import ShoppingConstants
from pages.base_page import BasePage
from pages.utils import log_decorator


class Header(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = HeaderConstants()
        self.login_page = LoginPageConstants()
        self.shopping_page = ShoppingConstants()

    @log_decorator
    def navigate_to_login(self):
        """Click on login button"""
        self.click(self.constants.LOGIN_BUTTON_XPATH)
        from pages.login_page import LoginPage
        return LoginPage(self.driver)

    @log_decorator
    def navigate_to_register(self):
        """Click on register button"""
        self.click(self.constants.REGISTER_BUTTON_XPATH)
        from pages.register_page import RegisteredPage
        return RegisteredPage(self.driver)

    @log_decorator
    def navigate_to_logout(self):
        """Click on logout button"""
        self.click(self.constants.LOG_OUT_BUTTON_XPATH)

    @log_decorator
    def verify_log_out_button(self):
        """Verify successful login using the log in button"""
        assert self.get_element_text(
            self.constants.LOG_IN_BUTTON_XPATH) == self.constants.LOG_IN_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.LOG_IN_BUTTON_XPATH)}"

    @log_decorator
    def navigate_to_shopping_cart(self):
        """Click on shopping cart button"""
        self.click(self.shopping_page.SHOPPING_BUTTON_XPATH)

    @log_decorator
    def verify_empty_shopping_cart(self):
        """Verify empty shopping cart"""
        assert self.get_element_text(
            self.shopping_page.SHOPPING_EMPTY_PRODUCTS_XPATH) == self.shopping_page.SHOPPING_EMPTY_PRODUCTS_TEXT, \
            f"Actual message: {self.get_element_text(self.shopping_page.SHOPPING_EMPTY_PRODUCTS_XPATH)}"
