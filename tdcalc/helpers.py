import math
from bizdays import Calendar, load_holidays

def truncate(x, n):
    '''
        Return x truncated to n decimal places.
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
    '''
        Return a bizdays Calendar instance initialized with ANBIMA brazilian
           holidays.
    '''
    holidays = load_holidays(holidays_file)
    return Calendar(holidays, ['Sunday', 'Saturday'], name='Brazil')

# https://www.investopedia.com/terms/e/effectiveinterest.asp
def eff_interest_rate(i, n):
    '''
        Return the effective interest rate of a nominal rate i and the number
            n of compounding periods.
    '''
    return pow(1 + i / n, n) - 1
