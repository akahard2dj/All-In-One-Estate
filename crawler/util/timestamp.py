import datetime


def timestamp_to_datetime(unix_time: (int,float), date_format='%Y-%m-%d %H:%M:%S') -> str:
    if isinstance(unix_time, int):
        output = datetime.datetime.fromtimestamp(unix_time).strftime(date_format)
    elif isinstance(unix_time, float):
        output = datetime.datetime.fromtimestamp(int(unix_time)).strftime(date_format)
    else:
        raise TypeError('unix_time type Error: required type is int(preferred) or float')

    return output
