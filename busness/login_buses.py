from handdles.login_haddles import LoginHaddles
class LoginBuess:
    def __init__(self,driver):
        self.driver = driver
        self.lh = LoginHaddles(self.driver)

    def logins(self,users,psds):
        try:
            self.lh.click_fouce()
            self.lh.click_login()
            self.lh.send_user(users)
            self.lh.send_psd(psds)
            self.lh.click_button()
        except BaseException as e:
            return False
        else:
            return True

