# -*- coding: utf-8 -*-


class ApiResponse:
    @staticmethod
    def set_data(task_node, error_code=0, error_msg="", **kwargs):
        """设置返回结果"""
        result_info = task_node.result_info
        result_info["error_code"] = error_code
        result_info["error_msg"] = error_msg
        result_info["data"].update(kwargs)
        return result_info

    @staticmethod
    def set_error(task_node, error_code, error_msg):
        """设置请求结果"""
        result_info = task_node.result_info
        result_info["error_code"] = error_code
        result_info["error_msg"] = error_msg
        result_info["data"] = {}
        return result_info

