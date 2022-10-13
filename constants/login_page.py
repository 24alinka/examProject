class LoginPageConstants:
    LOGIN_EMAIL_INPUT_XPATH = ".//input[@autofocus='autofocus']"
    LOGIN_PASSWORD_INPUT_XPATH = ".//input[@class='password']"
    LOGIN_CHECKBOX_XPATH = ".//input[@id='RememberMe']"
    LOGIN_CONFIRM_BUTTON_XPATH = ".//input[@class='button-1 login-button']"
    LOGIN_ERROR_MESSAGE_XPATH = ".//div[@class='validation-summary-errors']/span[contains(text(), " \
                                "'Login was unsuccessful. Please correct the errors and try again.')]"
    LOGIN_ERROR_MESSAGE_TEXT = "Login was unsuccessful. Please correct the errors and try again."
    LOGIN_FORGOT_PASSWORD_XPATH = ".//a[@href='/passwordrecovery']"
    LOGIN_EMAIL_FORGOT_XPATH = ".//input[@class='email']"
    LOGIN_RECOVER_BUTTON_XPATH = ".//input[@name='send-email']"
    LOGIN_SENT_YOU_XPATH = ".//div[@class = 'result']"
    LOGIN_SENT_YOU_TEXT = "Email with instructions has been sent to you."
