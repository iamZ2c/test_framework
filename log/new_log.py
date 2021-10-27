import logging
import os

LOG_FORMATTER = ('%(asctime)s - %(name)s - %(levelname)s - %(status)s- %(message)s',
                 '%H:%M:%S')

LOG_NAME = r'TestReport'

LOG_FILE = os.path.join(os.path.dirname(os.getcwd()), 'log', 'logs', 'TestReport.log')

LOG_LEVEL = logging.DEBUG


def create_logger(
        log_name: str = LOG_NAME,
        log_file: str = LOG_FILE,
        log_level: int = LOG_LEVEL,
        log_formatter: tuple = LOG_FORMATTER
):
    """
    日志配置生成器
    :param log_name:日志名称
    :param log_file:日志文件路径
    :param log_level:日志等级
    :param log_formatter:日志格式
    :return:
    """
    logger = logging.getLogger(log_name)
    logger.setLevel(log_level)

    formatter = logging.Formatter(*log_formatter)

    handler = logging.FileHandler(log_file, mode='a')

    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger


log = create_logger()

