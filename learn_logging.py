import os
import shutil
import logging
from logging.handlers import TimedRotatingFileHandler

FORMATTER = "[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s]%(message)s"


def init_logger(level=logging.DEBUG, path=None, name=None, clear=False, backup_count=0, console=True):
    # logger
    logger = logging.getLogger()

    # level
    logger.setLevel(level=level)

    if console:
        handler = logging.StreamHandler()
    else:
        path = path or "D://"
        name = name or "log.log"
        if clear and os.path.isdir(path):
            shutil.rmtree(path)
        if not os.path.isdir(path):
            os.makedirs(path)
        logfile = os.path.join(path, name)
        handler = TimedRotatingFileHandler(filename=logfile, when="midnight", backupCount=backup_count)

    # format
    # %(levelno)s：打印日志级别的数值
    # %(levelname)s：打印日志级别的名称
    # %(pathname)s：打印当前执行程序的路径，其实就是sys.argv[0]
    # %(filename)s：打印当前执行程序名
    # %(funcName)s：打印日志的当前函数
    # %(lineno)d：打印日志的当前行号
    # %(asctime)s：打印日志的时间
    # %(thread)d：打印线程ID
    # %(threadName)s：打印线程名称
    # %(process)d：打印进程ID
    # %(message)s：打印日志信息
    formatter = logging.Formatter(FORMATTER)
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger


if __name__ == '__main__':
    logger = init_logger(console=True)
    logger.info("Hello Logging")
