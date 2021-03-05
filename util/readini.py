import configparser
import os

class Readini():
    def __init__(self,file_path=None,node=None):
        if file_path==None:
            file_path = '../1.data/elementini.ini'
        if node == None:
            node = 'Login'
        else:
            node = node
        # 创建管理对象
        self.conf = configparser.ConfigParser()
        # 读ini文件
        self.conf.read(file_path, encoding="utf-8")

    def readini(self,key):
        #获取所有的section
        # sections = self.conf.sections()
        # print(sections)
        #获取某个sections中的所有值,将其转化为字典
        items = dict(self.conf.items(key))
        return items


if __name__ == '__main__':
    test = Readini()
    t = test.readini('Login')   #传入sections的值
    #print('我取某个sections下所有值 ',t)
    a = t['dingwei']
    print(a)
