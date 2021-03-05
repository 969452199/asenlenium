import time
import HTMLTestRunner
import unittest
#加载当前目录，与unittest02.py在同一个目录(一个.是当前目录；..是上级目录）
test_dir = '../case/'
#加载当前目录下以class开头的.PY文件
discover = unittest.defaultTestLoader.discover(test_dir,pattern='login_case.py')

#定义报告目录
file_dir = '../report/Report1/'

#定义报告名称格式
nowtime = time.strftime('%Y-%m-%d %H_%M_%S')
file_name = file_dir + nowtime + 'Report.html'
with open(file_name,'wb') as f:
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='测试报告',description='32143')
    runner.run(discover)