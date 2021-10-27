import logging
import os
import datetime


def get_time(func):
    print(datetime.datetime.now())
    return func


class UserLog:

    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.raiseExceptions)

        # 控制台输出日志
        self.console = logging.StreamHandler()
        self.logger.addHandler(self.console)

        # 文件输出日志
        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(base_dir, "logs")
        log_file = datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
        log_name = log_dir + "/" + log_file

        self.file_handle = logging.FileHandler(log_name, mode='a')
        self.file_handle.setLevel(logging.INFO)
        # 创建流后需要addhander进去
        self.logger.addHandler(self.file_handle)
        formatter = logging.Formatter(
            '%(asctime)s %(filename)s funcName:%(funcName)s lineno:%(lineno)d %(levelname)s %(message)s ')
        self.file_handle.setFormatter(formatter)

    @get_time
    def get_logger(self):
        return self.logger

    def logger_close(self):
        self.console.close()
        self.file_handle.close()
        self.logger.removeHandler(self.file_handle)
        self.logger.removeHandler(self.console)


# 测试代码
ul = UserLog()
# ul.get_logger()
