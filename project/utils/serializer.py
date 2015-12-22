__author__ = 'ali'

import datetime


def dump_datetime(time):
    """
    change datetime format
    :param: datetime
    :type : datetime.datetime
    :rtype : chagned datetime format
    """
    if datetime is None:
        return None
    if isinstance(time, datetime.datetime):
        return time.timestamp()


def dump_time(time):
    if time is None:
        return None
    return time.strftime("%H:%M:%S")