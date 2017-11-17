from tdcalc.helpers import truncate


def price(ytm, bdays):
    '''
        price(...) -> float truncated to the 6th decimal place

        Return the price of a National Treasury Bill (LTN) with ytm yield (to
           maturity) and bdays business days between the settlement date,
           inclusive, and the maturity date (exclusive). The yield follows
           a business days / 252 per year convention.
    '''
    nominal_value = 1000  # always 1,000 in this case
    ytm = truncate(ytm, 4)  # we must assure it is truncated to this precision
    years = truncate(bdays / 252, 14)
    price = nominal_value / pow(1 + ytm, years)
    return truncate(price, 6)
