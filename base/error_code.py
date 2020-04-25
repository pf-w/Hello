# -*- coding: utf-8 -*-


class ErrorCode:
    """错误码定义"""
    OK = 0

    INVALID_PARAM = 1   # 参数不合法
    USER_NOT_EXIST = 2      # 用户不存在
    LOGIN_ERROR = 3       # 登录失败
    PHONE_ERROR = 6     # 手机号不正确
    CM_PARAM_MISSED = 8     # 公共参数缺失
    TOKEN_EXPIRED = 9   # token过期
    UPDATE_ERROR = 10   # 用户信息更新失败
    NOT_EXIST = 30      # 记录不存在
    INTEGRITY_ERROR = 32    # 完整性错误
    INVALID_OPERATION = 33    # 无效操作
    DUPLICATED_OPERATION = 40  # 重复操作
    WRONG_OPERATION = 41    # 错误操作
    FAILED_VERIFICATION = 42    # 验证失败
