# -*- coding: utf-8 -*-

"""定义项目中所使用到的带参数的格式化Redis键和不带参数的Redis键
不同类型的键带有不同前缀, 规则如下:
------------------------------------------------------
键类型     前缀    示例
字符串      c_      c_XXXXX
列表        l_      l_XXXXXX
集合        s_      s_XXXXXX
有序集合    ss_      ss_XXXXX
哈希        h_      h_XXXXXXX
pubsub      ps_    ps_XXXXXX
hyperloglog hp_    ph_XXXXXX
-------------------------------------------------------
"""


class RedisKey:
    """
    不带参数的RedisKey
    """
    pass


class RedisKeyFormat:
    """
    带有格式化参数的RedisKey
    """
    pass
