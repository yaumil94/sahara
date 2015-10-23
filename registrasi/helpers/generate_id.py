import time
import datetime

class Generator(object):

    def __init__(self):
        pass

    def generate_from_date(self):
        current_day = datetime.datetime.now().strftime("%d")
        current_month = datetime.datetime.now().strftime("%m")
        current_year = datetime.datetime.now().strftime("%y")
        current_hour = datetime.datetime.now().strftime("%H")
        current_minute = datetime.datetime.now().strftime("%M")
        current_second = datetime.datetime.now().strftime("%s")[9:]
        return "{}{}{}{}{}{}".format(current_day, current_month, current_year,
            current_hour, current_minute, current_second
        )