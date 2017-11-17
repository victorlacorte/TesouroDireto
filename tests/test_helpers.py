from tdcalc.helpers import truncate, get_bizcalendar, eff_interest_rate


def test_truncate():
    assert truncate(1.4567, 2) == 1.45
    assert truncate(1.4447, 2) == 1.44
    assert truncate(-1.4567, 2) == -1.45
    assert truncate(1, 2) == 1
    assert truncate(-1, 2) == -1

def test_bizcalendar():
    cal = get_bizcalendar()
    assert cal.isbizday('2014-01-13')
    assert cal.bizdays('2014-01-13', '2015-01-13') == 253

def test_eff_interest_rate():
    i1 = 0.1
    n1 = 12
    assert round(eff_interest_rate(i1, n1), 4) == 0.1047
    i2 = 0.101
    n2 = 2
    assert round(eff_interest_rate(i2, n2), 4) == 0.1036
