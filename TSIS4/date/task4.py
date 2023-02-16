import datetime


def diff(t1, t2):
    return t1 - t2


print(diff(datetime.datetime.now(), datetime.datetime.now() - datetime.timedelta(days=1, hours=12, minutes=23)))

print(diff(datetime.datetime(2023, 2, 13), datetime.datetime(2023, 1, 5)));
