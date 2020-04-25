# -*- coding: utf-8 -*-
import json
from tornado import web
from tornado import escape
from tornado.log import gen_log
from tornado.web import RequestHandler
from base.error_code import ErrorCode
from base.task_node import TaskNode
from util.convert_util import obj_2_dict


class BaseHandler(RequestHandler):
    def prepare(self):
        # 允许跨域访问
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header(
            'Access-Control-Allow-Headers',
            'Origin, X-Requested-With, Content-Type, Accept, user-id, token, client-type, net'
        )

        self.task_node = TaskNode()
        self.seq_no = self.task_node.seq_no
        self.result_info = self.task_node.result_info

        self.params = self.task_node.params
        self.cm_params = self.task_node.cm_params   # 公共参数

        # MiddleWare

    def options(self):
        """询问请求方法"""
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept, user-id, token")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, DELETE, PUT')
        self.write({"error_code": " 0", "error_msg": ""})

    def get_param(self, param_name, default_value=""):
        """
        : param_name 参数名
        : default_value 默认值
        解析请求参数
        如果参数不存在, 则返回默认值; 否则将参数值转换成为默认值的类型再返回.
        对于 GET 请求, 从查询字符串获取参数; 对于 DELETE 请求, 参数先从BODY中取, 再从查询字符串中取;
        对于PUT和POST请求从BODY部分直接获取, 而不是从body_argument获取。这是因为
        我们定义的POST、GET、PUT请求的Content-Type都是application/json, tornado不对这种类型的请求解析body参数。
        """
        strip_str = lambda s: s if not isinstance(s, str) else s.strip()
        try:
            if self.request.method == 'GET':
                return type(default_value)(self.get_query_argument(param_name, default_value))
            elif self.request.method == 'DELETE':
                try:
                    json_param = escape.json_decode(self.request.body)
                    if param_name in json_param:
                        return strip_str(json_param.get(param_name))
                except json.decoder.JSONDecodeError:
                    pass
                return type(default_value)(self.get_query_argument(param_name, default_value))
            else:
                content_type = self.request.headers.get("Content-Type", "application/x-www-form-urlencoded")
                if content_type.startswith("application/json"):
                    json_param = escape.json_decode(self.request.body)
                    return type(default_value)(strip_str(json_param.get(param_name, default_value)))
                else:
                    return type(default_value)(self.get_argument(param_name, default_value))
        except ValueError as e:
            gen_log.error('<seq_no=%s>参数类型不正确, 异常信息: %s', self.task_node.seq_no, e)
            self.write({'error_no': ErrorCode.INVALID_PARAM, 'error_msg': '参数类型不正确'})
            raise web.Finish

    def write_result(self):
        """返回结果"""
        result_info = obj_2_dict(self.result_info)
        self.write(result_info)
        # 返回结果后，请求终止
        self.finish()
        return
