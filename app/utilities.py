from datetime import datetime
from hashlib import md5
from random import shuffle


def create_hash(shift):
    shift = str(shift)
    shift = md5(shift.encode('utf-8')).hexdigest()

    return shift


def create_hash_w_time(shift):
    currtime = datetime.now()
    shift = '{} {}'.format(shift, currtime)

    return create_hash(shift)


# Working with Jinja
def jinja_random_list(sequence, repeats=1):
    r = list(sequence)

    if (repeats >= 0):
        shuffle(r)
        return jinja_random_list(r, (repeats - 1))
    elif (repeats == 0):
        return r
    else:
        return sequence


def jinja_escape_hash(shift):
    return create_hash_w_time(shift)