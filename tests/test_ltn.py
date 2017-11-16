from tdcalc import ltn
from tdcalc.helpers import get_bizcalendar


# Dates always YYYY-MM-DD
cal = get_bizcalendar()

def test_price():
    maturity = '2010-07-01'
    settlement = '2008-05-21'
    ytm = 0.1436
    bdays = cal.bizdays(settlement, maturity)
    assert bdays == 532
    price = ltn.price(ytm, bdays)
    assert price == 753.315323
