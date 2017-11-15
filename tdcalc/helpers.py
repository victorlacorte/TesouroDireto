import math
from bizdays import Calendar, load_holidays

def truncate(x, n):
    '''
        Return x truncated to n decimal places
    '''
    # https://stackoverflow.com/questions/20544714/truncate-a-decimal-value-in-python
    # Possibly also:
    # https://stackoverflow.com/questions/783897/truncating-floats-in-python
    p = pow(10, n)

    if x < 0:
        return math.ceil(x * p) / p
    else:
        return math.floor(x * p) / p

def get_bizcalendar(holidays_file='tdcalc/data/anbima.txt'):
    holidays = load_holidays(holidays_file)
    return Calendar(holidays, ['Sunday', 'Saturday'], name='Brazil')
