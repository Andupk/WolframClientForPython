# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

from wolframclient.utils.date import new_date, new_datetime, new_time

import datetime

NOW = datetime.datetime(
    year   = 2000,
    month  = 1,
    day    = 1,
    hour   = 11,
    minute = 15,
    second = 20
)

def test_datetime(tzinfo = None):
    return new_datetime(NOW, NOW, tzinfo = tzinfo)

def test_date():
    return new_date(NOW)

def test_time(tzinfo = None):
    return new_time(NOW, tzinfo = tzinfo)