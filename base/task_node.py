# -*- coding: utf-8 -*-
import time


class TaskNode:
    """
    请求任务结点, 包括请求的输入/输出, 以及相关的中间信息
    Attributes:
        seq_no:             @str, 请求的序列号
        cm_param:       @dict, 请求的公共参数
        bl_param:     @dict, 请求的业务参数
        start_datetime:     @datetime, 请求处理的起始时间戳
        start_timestamp:    @float, 请求处理的起始时间戳
        scan_timestamp:     @float, 统计耗时的计时时间戳, 每次计算耗时后都更新到当前时间点
        timecost_list:      @list, 处理的耗时信息, (str(tc_name), float(tc_val))
        landmarks:          @list, 请求处理过程中重要节点的信息
    Methods:
        set_step_timecost: 添加步骤的耗时, 单位ms
        set_landmark_data: 添加节点信息数据
    """
    __start_timestamp = time.time()

    def __init__(self):
        self.cm_params = {}     # 公共参数
        self.params = {}
        self.seq_no = self.__start_timestamp
        self.scan_timestamp = self.__start_timestamp
        self.timecost_list = []
        self.result_info = {"error_code": " 0", "error_msg": "", "data": {}}

    def set_step_duration(self, step_name):
        new_timestamp = time.time()
        step_timecost = "%.2f" % (1000.0 * (new_timestamp - self.scan_timestamp))  # ms
        self.timecost_list.append((step_name, step_timecost))
        self.scan_timestamp = new_timestamp
