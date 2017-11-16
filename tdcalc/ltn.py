from tdcalc.helpers import truncate

def price(ytm, bd):
    '''
        Return the price of a National Treasury Bill (LTN)


        ytm (yield to maturity) - business days / 252 per year convention,
           truncated to the 4th decimal place. Known on purchase

        bd - number of business days between the settlement date, inclusive,
           and the maturity date (exclusive)
    '''
    unv = 1000  # always 1,000 in this case
    delta = truncate(bd / 252, 14)
    price = unv / pow(1 + ytm, delta)
    return truncate(price, 6)
