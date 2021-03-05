from base.find_element import Findelement
class Loginpages:
    def __init__(self,driver):
        self.driver = driver
        self.find = Findelement(self.driver)

    def get_fouce(self):
        return self.find.findelement(node='Login',key='dingwei')

    def get_login(self):
        return self.find.findelement(node='Login',key='jiemian')

    def get_user(self):
        return self.find.findelement(node='Login',key='loguser')


    def get_psd(self):
        return self.find.findelement(node='Login',key='logpsd')


    def get_button(self):
        return self.find.findelement(node='Login',key='denglu')
