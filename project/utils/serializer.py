__author__ = 'ali'

import datetime


def dump_datetime(value):
    """
    change datetime format
    :param: datetime
    :type : datetime.datetime
    :rtype : chagned datetime format
    """
    if datetime is None:
        return None
    if isinstance(value, datetime.datetime):
        return value.timestamp() * 1000


def dump_time(time):
    if time is None:
        return None
    return time.strftime("%H:%M:%S")