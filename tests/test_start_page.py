import logging


class TestStartPage:
    log = logging.getLogger("[StartPage]")

    def test_newsletter1(self, start_page):
        """
        - Pre-conditions:
            - Create driver
            - Open page
        - Steps:
            - Fill random email
            - Click button
            - Verify success message
        - Post-conditions:
            - Close driver
        """
        # Fill email and click on the Subscribe button
        start_page.subscribe("tes232223232t@test.test")
        # Verify success message
        start_page.verify_subscribe()
        self.log.info("The user has subscribed.")

    def test_empty_subscribe(self, start_page):
        """
        - Pre-conditions:
            - Create driver
            - Open page
        - Steps:
            - Click button
            - Verify error message
        - Post-conditions:
            - Close driver
        """
        # Fill empty string email
        start_page.subscribe("")
        # Click on the Subscribe button
        start_page.click_on_subscribe_button()
        # Verify error message
        start_page.verify_error_message()
        self.log.info("The error was verified.")

    def test_add_a_product_to_shopping_cart(self, start_page):
        """
        - Pre-conditions:
            - Create driver
            - Open page
        - Steps:
            - Click on the product
            - Add a product to the shopping cart
            - Verify added product to the shopping cart
        - Post-conditions:
            - Close driver
        """
        # Click on the product and add a product to the shopping cart
        start_page.click_on_the_product_and_add_to_the_shopping_cart()
        # Verify added product to the shopping cart
        start_page.verify_added_product_to_the_shopping_cart()
        self.log.info("The product was added")