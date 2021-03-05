from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from util.readini import Readini
import time
class Findelement:
    def __init__(self,driver):
        self.driver = driver


    def findelement(self,node=None,key=None):
        de = Readini()
        er = de.readini(node)
        value = er[key]
        b = value.split('>')
        print(b[0],b[1])
        try:
            if b[0] == 'id':
                #WebDriverWait(driver=driver,timeout=20).until(EC.presence_of_element_located(tuple(b)))
                return self.driver.find_element_by_id(b[1])
            elif b[0] == 'classname':
                #WebDriverWait(driver=driver, timeout=20).until(EC.presence_of_element_located(tuple(b)))
                return self.driver.find_element_by_class_name(b[1])
            else:
                #WebDriverWait(driver=driver, timeout=20).until(EC.presence_of_element_located(tuple(b)))
                return self.driver.find_element_by_xpath(b[1])
        except BaseException as e:
            print(e)
            #return None

if __name__=='__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get('https://www.lagou.com/')
    t = Findelement(driver=driver)
    time.sleep(3)
    t.findelement(node='Login',key='dingwei')

