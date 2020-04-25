# -*- coding: utf-8 -*-
import os
import logging
from cloghandler import ConcurrentRotatingFileHandler
from tornado.log import LogFormatter, access_log, app_log, gen_log

from conf.hello_conf import ServerConfig


class InitLogger:
    __fmt = "%(color)s[%(levelname)1.1s %(asctime)s {port} %(module)s:%(funcName)s:%(lineno)d]%(end_color)s %(message)s"

    @classmethod
    def init_logger(cls, port):
        formatter = LogFormatter(fmt=cls.__fmt.format(port=port), datefmt="", color=False)

        access_log_handler = ConcurrentRotatingFileHandler(
            filename=os.path.join(ServerConfig["log_dir"], "access.log")
        )
        access_log_handler.setFormatter(formatter)
        access_log.addHandler(access_log_handler)

        server_log_handler = ConcurrentRotatingFileHandler(
            filename=os.path.join(ServerConfig['log_dir'], 'server.log'),
            maxBytes=128 * 1024 * 1024,
            backupCount=5,
            encoding='utf8'
        )
        server_log_handler.setFormatter(formatter)
        gen_log.addHandler(server_log_handler)
        app_log.addHandler(server_log_handler)

        access_log.setLevel(logging.INFO)
        gen_log.setLevel(getattr(logging, ServerConfig['log_level'].upper()))
        app_log.setLevel(getattr(logging, ServerConfig['log_level'].upper()))

        access_log.propagate = app_log.propagate = gen_log.propagate = False
        return
