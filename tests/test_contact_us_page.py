import logging
from pages.utils import ContactUs


class TestContactUs:
    log = logging.getLogger("[ContactUs]")

    def test_sent_message(self, start_page):
        """
        - Pre-conditions:
            - Create driver
            - Open page
        - Steps:
            - Click on the Contact Us button
            - Fill data and sent message
            - Verify success message
        - Post-conditions:
            - Close driver
        """
        # Navigate to create Post Page
        start_page.footer.navigate_to_contact_page()
        # Sent message
        contact = ContactUs()
        contact.fill_default(contact.name, contact.email)
        start_page.contact_us_page.create_message(contact)
        # Verify success message
        start_page.contact_us_page.verify_successfully_sent_message()
        self.log.info("Sending message is checked.")

    def test_empty_message(self, start_page):
        """
        - Pre-conditions:
            - Create driver
            - Open page
        - Steps:
            - Click on the Contact Us button
            - Fill data with empty message and sent message
            - Verify error message
        - Post-conditions:
            - Close driver
        """
        # Navigate to create Post Page
        start_page.footer.navigate_to_contact_page()
        # Sent message
        contact = ContactUs()
        contact.fill_default(contact.name, contact.email)
        start_page.contact_us_page.create_message(contact)
        # Verify success message
        start_page.contact_us_page.verify_successfully_sent_message()
        self.log.info("The error was verified.")