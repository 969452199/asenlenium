#1.创建元素.ini文件data/element.ini
#2.创建util包，编写读取文件脚本，util/readini.py
#3.创建base包，编写元素定位脚本，base/find_element.py
#4.创建pages包，编写文件参数引入元素定位脚本，pages/login_pages
#5.创建handdles包，编写操作流程（点击或传值），handdles/login_haddles
#6.创建busness包，引用函数并设置结果（TRUE/FOUSE），busness/login_buses
#7.创建case包，编写案例，引用创建busness函数，使用dtt数据驱动



from busness.login_buses import LoginBuess
from selenium import webdriver
import time
from ddt import ddt,data,unpack
import unittest
from main import loggging
#
log =loggging.logers(loggging.creat_file(), level='debug')
log.loger.debug('debug')

@ddt
class LoginCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://www.lagou.com/')
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()
        cls.lb = LoginBuess(cls.driver)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    @data({'users':'18702594561','psds':'xu187025945610'})
    @unpack
    def test_login(self,users,psds):
        logng = self.lb.logins(users,psds)
        self.assertTrue(logng)

if __name__=='__main__':
    unittest.main()