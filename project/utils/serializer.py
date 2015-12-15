__author__ = 'ali'


def dump_datetime(datetime):
    """
    change datetime format
    :param: datetime
    :type : datetime.datetime
    :rtype : chagned datetime format
    """
    if datetime is None:
        return None
    return datetime.strftime("%Y-%m-%d-%H:%M:%S")


def dump_time(time):
    if time is None:
        return None
    return time.strftime("%H:%M:%S")