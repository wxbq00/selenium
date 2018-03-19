# import logging
# from logging.handlers import TimedRotatingFileHandler
# from case.config.config import LOG_PATH
#
#
# class Logger(object):
#     def __init__(self, logger_name='framework'):
#         self.logger = logging.getLogger(logger_name)
#         logging.root.setLevel(logging.NOTSET)
#         self.log_file_name = 'test.log'
#         self.backup_count = 5
#         # 日志输出级别
#         self.console_output_level = 'WARNING'
#         self.file_output_level = 'DEBUG'
#         # 日志输出格式
#         self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
#     def get_logger(self):
#         """在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回"""
#         if not self.logger.handlers:  # 避免重复日志
#             console_handler = logging.StreamHandler()
#             console_handler.setFormatter(self.formatter)
#             console_handler.setLevel(self.console_output_level)
#             self.logger.addHandler(console_handler)
#
#             # 每天重新创建一个日志文件，最多保留backup_count份
#             file_handler = TimedRotatingFileHandler(filename=LOG_PATH + self.log_file_name,
#                                                     when='D',
#                                                     interval=1,
#                                                     backupCount=self.backup_count,
#                                                     delay=True,
#                                                     encoding='utf-8'
#                                                     )
#             file_handler.setFormatter(self.formatter)
#             file_handler.setLevel(self.file_output_level)
#             self.logger.addHandler(file_handler)
#         return self.logger
#
# logger = Logger().get_logger()
#
#

# coding:utf-8
import logging, time, os
# 这个是日志保存本地的路径
from case.config.config import LOG_PATH
class Log:
    def __init__(self):# 文件的命名
        self.logname = os.path.join(LOG_PATH, '%s.log' % time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')
    def __console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        fh = logging.FileHandler(self.logname, 'a')# 追加模式
        # fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')  # 这个是python3的
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)
    # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
            # 这两行代码是为了避免日志输出重复问题
            self.logger.removeHandler(ch)
            self.logger.removeHandler(fh)
            # 关闭打开的文件
            fh.close()
    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)
if __name__ == "__main__":
    log = Log()
    log.info("---测试开始----")
    log.info("输入密码")
    log.warning("----测试结束----")


