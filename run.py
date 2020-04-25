# -*- coding: utf-8 -*-
import os
from tornado import ioloop  # 核心IO循环
from tornado import httpserver  # 异步非阻塞的HTTP服务器模块
from tornado import web    # web框架模块
from tornado import options  # 解析终端命令行参数
from tornado.options import define, options     # define用于获取终端命令行参数，options用于设置参数

from conf.hello_conf import ServerConfig
from urls import handlers
from base.init_logger import InitLogger


# 如果命令行中有port参数，则将port参数设置到options中，若没有则使用default
# define(name="port", default=8080, type=int, help="--port: 端口号")
# define(name="debug", default=False, type=bool, help="--debug: 调试模式")


def run():
    settings = {
        'static_path': os.path.join(os.path.dirname(__file__), 'static'),
        'template_path': os.path.join(os.path.dirname(__file__), 'template')
    }
    # 解析命令行参数
    # options.parse_command_line()

    port = ServerConfig["port"]
    InitLogger.init_logger(port)

    # 创建应用实例
    app = web.Application(
        handlers=handlers,
        debug=options.debug,
        **settings
    )
    # app.listen(options.port)

    # 手动创建服务器
    # HTTPServer(app)中的app是为了让服务器到app中匹配路由，并只能匹配app中路由，
    # 若客户端输入app中没有的路由则报错
    http_server = httpserver.HTTPServer(app)
    # 监听端口
    http_server.listen(port)
    """
    httpServer.listen和app.listen不一样，两个listen表示不一样的对象，就好比小明有10元，小红也有10元，对象不同
    app.listen()等同于 httpServer = tornado.httpserver.HTTPServer(app)+httpServer.listen()
    使用 httpServer = tornado.httpserver.HTTPServer(app)+httpServer.listen()该方法是更加直观的如何启动服务器
    """

    # 创建IOLoop实例并启动
    ioloop.IOLoop.current().start()


if __name__ == "__main__":
    run()
