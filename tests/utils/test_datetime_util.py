# -*- coding: utf-8 -*-
"""
@File    : test_datetime_util.py
@Date    : 2023-07-24
"""
import time
from datetime import datetime

from domain_admin.utils import datetime_util


def test_time_for_human():
    print(datetime_util.time_for_human(1665381270))
    # 2天前

    print(datetime_util.time_for_human(datetime.now()))
    # 刚刚

    print(datetime_util.time_for_human(time.time() - 100))
    # 1分钟前

    print(datetime_util.time_for_human('2022-10-10 13:33:11'))
    # 2天前

    print(datetime_util.get_timestamp(datetime.now()))

def test_time_for_human2():
    start = '2023-07-24 08:54:19'
    end = '2023-07-24 09:07:05'
    start = datetime_util.parse_datetime(start)
    end = datetime_util.parse_datetime(end)

    print("\n")
    print(datetime_util.get_diff_time(start, end))
    print(datetime_util.seconds_for_human(datetime_util.get_diff_time(start, end)))
