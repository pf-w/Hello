# -*- coding: utf-8 -*-
import random

from tornado.log import gen_log

from base.api_response import ApiResponse


class Hello:
    @classmethod
    async def get_data(cls, task_node):
        angle = random.randint(0, 360)
        gen_log.info("<seq_no=%s>生成旋转角度, angle=%s", task_node.seq_no, angle)
        colors = cls.gen_colors(2)
        gen_log.info("<seq_no=%s>生成颜色, colors=%s", task_node.seq_no, colors)
        return ApiResponse.set_data(task_node, angle=angle, colors=colors)

    @classmethod
    def gen_colors(cls, count: int):
        gen_color = lambda: random.randint(0, 255)
        color_fmt = "#%02X%02X%02X"
        colors = []
        for i in range(count):
            colors.append(color_fmt % (gen_color(), gen_color(), gen_color()))
        return colors
