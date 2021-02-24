# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author : mao
import arrow

from datetime import datetime
from datetime import timedelta


class TimeUtils:
    _today = datetime.today()
    _now = datetime.now()
    _iteration_period = 14

    def __init__(self):
        pass

    def __str__(self):
        return "TimeUtils: A Tool For Processing Time."

    @classmethod
    def _calculation_iter(cls, iteration_end_time, time_str, iter_count):
        """
        :param iteration_end_time: Iteration End Time
        :type iteration_end_time: datetime
        :param time_str: A standard time string
        :type time_str: str
        :param iter_count: Iterations
        :type iter_count: int
        :return:
        """
        for _ in range(iter_count - 1, -1, -1):
            yield (iteration_end_time - timedelta(days=cls._iteration_period*_)).strftime(time_str)

    @staticmethod
    def str_to_datetime(date_string, date_format):
        """
        Convert string to time format
        :param date_string: Time String
        :type date_string: str
        :param date_format: Time format
        :type date_format: str
        :return: datetime
        """
        return datetime.strptime(date_string, date_format)

    @classmethod
    def datetime_format_week_str(cls, date_string, format_str):
        """
        Gets the number of weeks for formatting, for Example: 2021年第1周
        :param date_string: Time String
        :type date_string: str
        :param format_str: Time format
        :type format_str: str
        :return:
        """
        _date = cls.str_to_datetime(date_string, format_str)
        return "%s年第%s周" % _date.isocalendar()[:2]

    @classmethod
    def get_day_iter_list(cls, iter_start_time, format_str, iterations):
        """
        Gets a list of iterations based on date.
        :type iter_start_time: str
        :param iter_start_time: Iteration start time, for Example: '2020-08-25'
        :type format_str: str
        :param format_str: A standard time string, for Example: '%Y-%m-%d' or '%Y%m%d'
        :type iterations: int
        :param iterations: Iterations
        :return:
        """
        _time = cls.str_to_datetime(iter_start_time, format_str)
        time_difference = cls._today.__sub__(_time)
        iter_count_num = int(time_difference.days / cls._iteration_period) \
            if time_difference.days > 0 else (- int(abs(time_difference.days) / cls._iteration_period) - 1)
        end_iter_time = _time + timedelta(days=iter_count_num * cls._iteration_period)
        iter_time_list = [_ for _ in cls._calculation_iter(end_iter_time, format_str, iterations)]
        return iter_time_list

    @staticmethod
    def get_month_iter_list(year, month, cycle):
        """
        Gets a list of iterations based on month.
        :param year: Year of iteration date
        :type year: str
        :param month: Month of iteration date
        :type month: int
        :param cycle: cycle of iteration date numbers
        :type cycle: int
        :return: A iterations Month list
        """
        _date = f"{year}-{month if month >= 10 else f'0{month}'}"
        _date = arrow.get(_date, 'YYYY-MM')
        month_list = [_date.shift(months=-i).format('YYYY-MM') for i in range(cycle - 1, -1, -1)]
        return month_list

    @classmethod
    def get_last_cycle(cls, _type, week):
        """
        Get last cycle
        :param _type: Is it the start time, for Example: True
        :type _type: bool
        :param week: End with the day of the week in
        (0：Monday, 1：Tuesday, 2：Wednesday, 3：Thursday, 4：Friday, 5：Saturday, 6：Sunday)
        :type week: int
        :return: A string format datetime
        """
        if week not in (0, 1, 2, 3, 4, 5, 6):
            return Exception('The week not in (0, 1, 2, 3, 4, 5, 6)')
        end_time = cls._now
        one_day = timedelta(days=1)
        while end_time.weekday() != week:
            end_time -= one_day
        return (end_time - timedelta(days=week)).strftime('%Y-%m-%d') if _type else end_time.strftime('%Y-%m-%d')

    @classmethod
    def get_last_cycle_list(cls, end_time_str, time_format, week, count, is_process=False):
        """
        Get last cycle list
        :param end_time_str: End time in the cycle
        :type end_time_str: str
        :param time_format: Time format
        :type time_format: str
        :param week: End with the day of the week in
        (0：Monday, 1：Tuesday, 2：Wednesday, 3：Thursday, 4：Friday, 5：Saturday, 6：Sunday)
        :type week: int
        :param count: Several iteration cycle, for Example: 7
        :type count: int
        :param is_process: None
        :type is_process: bool
        :return: A list of cycle times
        """
        if week not in (0, 1, 2, 3, 4, 5, 6):
            return Exception('The week not in (0, 1, 2, 3, 4, 5, 6)')
        end_time = cls.str_to_datetime(end_time_str, time_format)
        one_day = timedelta(days=1)
        while end_time.weekday() != week:
            end_time -= one_day
        date_list = [(end_time - timedelta(days=(1 if is_process else week + 1)*i)).strftime(time_format)
                     for i in range(count - 1, -1, -1)]
        return date_list

    @classmethod
    def get_after_day(cls, date_str, date_format, count):
        """
        Get after day
        :param date_str: Date String
        :type date_str: str
        :param date_format: Date format
        :type date_format: str
        :param count: How many days?
        :type count: int
        :return:
        """
        _date = cls.str_to_datetime(date_str, date_format)
        return (_date + timedelta(days=+count)).strftime(date_format)

    @classmethod
    def get_before_day(cls, date_str, date_format, count):
        """
        Get before day
        :param date_str: Date String
        :type date_str: str
        :param date_format: Date format
        :type date_format: str
        :param count: How many days?
        :type count: int
        :return:
        """
        _date = cls.str_to_datetime(date_str, date_format)
        return (_date + timedelta(days=-count)).strftime(date_format)
