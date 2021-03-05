import logging
from logging import handlers
import os.path
import time
class logers(object):
    level_relations = {'debug' : logging.DEBUG,
                       'info':logging.INFO,
                       'error':logging.ERROR,
                       'warn':logging.WARN,
                       'critical':logging.CRITICAL}

    def __init__(self,filename,level='info',when='D',backcount=3,fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.loger = logging.getLogger(filename)
        formater_str = logging.Formatter(fmt)
        self.loger.setLevel(self.level_relations.get(level))
        sh = logging.StreamHandler()
        sh.setFormatter(formater_str)
        th = handlers.TimedRotatingFileHandler(filename=filename,when=when,backupCount=backcount,encoding='utf-8')
        th.setFormatter(formater_str)
        self.loger.addHandler(sh)
        self.loger.addHandler(th)

def creat_file():
    rq = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
    log_data = rq[:6]
    log_path = os.getcwd()+'/Logs/{}/'.format(log_data)
    isExists = os.path.exists(log_path)
    if not isExists:
        os.makedirs(log_path)
    log_name = log_path + rq[:8] + '.log'
    return log_name

if __name__ == '__main__':
    log = logers(creat_file(),level='debug')
    log.loger.debug('debug')