from datetime import datetime
from hashlib import md5
from time import sleep


def log_msg(msg):
    dt = datetime.now()
    dh = dt.hour
    dm = dt.minute
    ds = dt.second

    timing = '{}:{}:{}'.format(dh, dm, ds)
    timing_sec = md5(timing.encode()).hexdigest()

    print('[ {} {} ] {}'.format(timing, timing_sec, msg))
    sleep(0.5)
