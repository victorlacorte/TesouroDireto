from tdcalc.helpers import truncate, get_bizcalendar


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
