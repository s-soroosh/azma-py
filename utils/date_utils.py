__author__ = 'soroosh'
from jdatetime import datetime as jalali_datetime


def greg_date_from_shamsi(date, splitter):
    parts = date.split(splitter)
    gregorian_date = jalali_datetime(int(parts[0]), int(parts[1]),
                                     int(parts[2])).togregorian()
    return gregorian_date