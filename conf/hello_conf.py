# -*- coding: utf-8 -*-

from tornado.options import define, options

define(name="port", default=8080, type=int, help="--port: 端口号")
define(name="debug", default=False, type=bool, help="--debug: 调试模式")
define(name="log_dir", default="./log", type=str, help="--log_dir: 日志路径")
define(name="log_level", default="DEBUG", type=str, help="--log_level: 日志级别")

options.parse_command_line()

ServerConfig = {
    "port": options.port,
    "log_dir": options.log_dir,
    "log_level": options.log_level,
}
