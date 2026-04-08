import sys
from icalendar import Calendar, Event, Alarm
from datetime import datetime, timedelta

def create_base_calendar():
    cal = Calendar()
    cal.add('prodid', '-//Smart School//CN')
    cal.add('version', '2.0')
    return cal

# 此脚本供 AI 调用执行，生成带前晚21点提醒的日历
