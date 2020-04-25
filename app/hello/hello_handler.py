# -*- coding: utf-8 -*-
from tornado.log import gen_log
from tornado.web import RequestHandler

from app.hello.hello import Hello
from base.base_handler import BaseHandler


class HelloHandler(BaseHandler):
    async def get(self):
        is_json = self.get_param("is_json", 0)
        if not is_json:
            gen_log.info("<seq_no=%s>渲染Hello页面")
            return self.render("hello.html")
        else:
            await Hello.get_data(self.task_node)
            return self.write_result()
