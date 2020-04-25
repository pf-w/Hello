# -*- coding: utf-8 -*-

from datetime import datetime, date
from decimal import Decimal


def obj_2_dict(obj, class_key=None):
    if isinstance(obj, str):
        return obj
    elif isinstance(obj, dict):
        data = {}
        for k, v in obj.items():
            data[k] = obj_2_dict(v, class_key)
        return data
    elif hasattr(obj, '__iter__'):
        return [obj_2_dict(v, class_key) for v in obj]
    elif hasattr(obj, '__dict__'):
        data = {}
        for k, v in obj.__dict__.items():
            if not k.startswith('_') and not callable(v):
                data[k] = obj_2_dict(v, class_key)
            if class_key is not None and hasattr(obj, '__class__'):
                data[class_key] = obj.__class__.__name__
        for k in dir(obj):
            if not k.startswith('_') and not callable(k) and k not in data:
                data[k] = obj_2_dict(getattr(obj, k), class_key)
        return data
    elif isinstance(obj, Decimal):
        return float(obj)
    elif isinstance(obj, datetime):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(obj, date):
        return obj.strftime('%Y-%m-%d')
    else:
        return obj
