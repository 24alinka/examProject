import logging
from pages.utils import User


class TestHeader:
    log = logging.getLogger("[Header]")

    def test_valid_login(self, start_page):
        """
        - Pre-conditions:
            - Create driver
            - Open page
        - Steps:
            - Fill email and password
            - Click button
            - Verify success log out
        - Post-conditions:
            - Close driver
        """
        # Click on Log In button
        login_page = start_page.header.navigate_to_login()
        # Fill data
        login_page.login_form(email="testetete@testt.test", password="testtest")
        # Click on the Log Out button
        start_page.header.navigate_to_logout()
        # Verified Log out
        start_page.header.verify_log_out_button()
        self.log.info("The valid login was verified.")

    def test_not_valid_log_in(self, start_page):
        """
        - Pre-conditions:
            - Create driver
            - Open page
        - Steps:
            - Click on log in button
            - Fill email and password
            - Click button
            - Verify error message
        - Post-conditions:
            - Close driver
        """
        # Click on Log In button
        login_page = start_page.header.navigate_to_login()
        # Fill email and password (user who is not registered)
        login_page.login_form(email="testalinka@test.com", password="testtest")
        # Verified error message
        start_page.login_page.verify_log_in_error()
        self.log.info("The not valid login was verified.")

    def test_forgot_password(self, start_page):
        """
        - Pre-conditions:
            - Create driver
            - Open page
        - Steps:
            - Click on Log In button
            - Click forgot password
            - Enter valid email
            - Click on Recover button
            - Verify sent message
        - Post-conditions:
            - Close driver
        """
        # Click on Log In button
        login_page = start_page.header.navigate_to_login()
        # Click forgot password
        start_page.login_page.click_forgot_button()
        # Enter valid email
        login_page.email_for_forgot_password(email="testetete@testt.test")
        # Verify sent message
        start_page.login_page.verify_sent_email()
        self.log.info("The forgot password was verified.")

    def test_valid_registration(self, start_page):
        """
        - Pre-conditions:
            - Create driver
            - Open page
        - Steps:
            - Click on the Register button
            - Fill data
            - Click button
            - Verify successful registration
        - Post-conditions:
            - Close driver
        """
        # Click on the Register button
        start_page.header.navigate_to_register()
        # Fill data and click ob the register button
        user = User()
        user.fill_data(password="test5678789", confirm_password="test5678789")
        start_page.register_page.register_form(user)
        # Verify successful message
        start_page.register_page.verify_successful_registration()
        self.log.info("The valid registration was verified.")

    def test_invalid_email_registration(self, start_page):
        """
        - Pre-conditions:
            - Create driver
            - Open page
        - Steps:
            - Click on the Register button
            - Fill data
            - Click button
            - Verify successful registration
        - Post-conditions:
            - Close driver
        """
        # Click on the Register button
        start_page.header.navigate_to_register()
        # Fill data and click on the register button
        user = User()
        user.fill_data(email="test@@alinka.com", password="test5678789", confirm_password="test5678789")
        start_page.register_page.register_form(user)
        # Verify error message
        start_page.register_page.verify_wrong_email()
        self.log.info("The error was verified.")

    def test_empty_shopping_cart(self, start_page):
        """
        - Pre-conditions:
            - Create driver
            - Open page
        - Steps:
            - Click on the Shopping cart button
            - Verify empty shopping cart
        - Post-conditions:
            - Close driver
        """
        # Click on the Shopping cart button
        start_page.header.navigate_to_shopping_cart()
        # Verify empty shopping cart
        start_page.header.verify_empty_shopping_cart()
        self.log.info("The empty shopping cart was verified.")