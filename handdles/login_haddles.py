from pages.login_pages import Loginpages

class LoginHaddles:
    def __init__(self,driver):
        self.driver = driver
        self.lp = Loginpages(self.driver)

    def click_fouce(self):
        self.lp.get_fouce().click()

    def click_login(self):
        self.lp.get_login().click()

    def send_user(self,users):
        self.lp.get_user().send_keys(users)

    def send_psd(self,psds):
        self.lp.get_psd().send_keys(psds)

    def click_button(self):
        self.lp.get_button().click()
