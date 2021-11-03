# -*- coding: utf-8 -*-
import logging
import os
import datetime
from config import globalparam

class loggerClass:
    # 日志级别的字典
    level_relation = {"debug": logging.DEBUG, "info": logging.INFO, "warning": logging.WARNING,
                      "error": logging.ERROR, "critical": logging.CRITICAL}
    # 日志输出格式
    fmt_str = "%(asctime)s | %(lineno)s | %(name)s | %(levelname)s | %(filename)s | %(funcName)s | %(message)s"
    logFile = globalparam.log_path

    def __init__(self, level = 'info', fmt = fmt_str):
      #  change_dir = os.chdir("G:/8.python/pytest_testApi")  # 切换工作目录
      #   if not os.path.exists(self.logFile):
      #       os.makedirs(self.logFile)
        formatter = logging.Formatter(fmt)
        # 生成以当天日期为名称的日志文件
        filename =self.logFile+'/'+'test_'+datetime.datetime.today().strftime('%Y-%m-%d')+'.log'

        # 初始化日志类参数
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(self.level_relation.get(level))

        # 定义日志输出到前面定义的filename中
        self.filelogger = logging.FileHandler(filename)
        # 定义日志输出格式
        self.filelogger.setFormatter(formatter)

    def info(self,message,level = "info"):
        '''
        # 日志输出到控制台
        console = logging.StreamHandler()
        self.logger.addHandler(console)
        '''
        self.logger.addHandler(self.filelogger)
        if level == "debug" or level == "DEBUG":
            self.logger.debug(message)
        elif level == "info" or level == "INFO":
            self.logger.info(message)
        elif level == "warning" or level == "WARNING":
            self.logger.warning(message)
        elif level == "error" or level == "ERROR":
            self.logger.error(message)
        elif level == "critical" or level == "CRITICAL":
            self.logger.critical(message)
        else:
            raise ("日志级别错误")
        self.logger.removeFilter(self.filelogger)

    def debug(self,message,level = "debug"):
        self.logger.addHandler(self.filelogger)
        if level == "debug" or level == "DEBUG":
            self.logger.debug(message)
        elif level == "info" or level == "INFO":
            self.logger.info(message)
        elif level == "warning" or level == "WARNING":
            self.logger.warning(message)
        elif level == "error" or level == "ERROR":
            self.logger.error(message)
        elif level == "critical" or level == "CRITICAL":
            self.logger.critical(message)
        else:
            raise ("日志级别错误")
        self.logger.removeFilter(self.filelogger)

# logger = loggerClass('debug')   # 设置日志对象接受的输出级别
# logger.info('测试的日志输出INFO','INFO')
# logger.info('测试的日志输出ERROR','ERROR')
# logger.info('测试的日志输出WARNING','WARNING')
# logger.info('测试的日志输出DEBUG','DEBUG')
#
# logger1 = loggerClass('warning')   #设置日志对象接受的输出级别
# logger1.info('测试的日志输出INFO','INFO')
# logger1.info('测试的日志输出ERROR','ERROR')
# logger1.info('测试的日志输出WARNING','WARNING')
# logger1.info('测试的日志输出DEBUG','DEBUG')