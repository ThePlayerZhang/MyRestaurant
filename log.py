import datetime
from setting import *


def TimeNow(strftime=log_Strftime):
    return datetime.datetime.now().strftime(strftime)
