# -*- coding: utf-8 -*-
from tornado.web import url
from app.hello.hello_handler import HelloHandler


urls = [
    url(r"/hello|/hello/", HelloHandler, name="hello"),
    url(r"/color", HelloHandler, name="color"),
]