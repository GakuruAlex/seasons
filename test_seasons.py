import pytest
from seasons import days_to_minutes, seasons, get_date


@pytest.mark.parametrize("date_of_birth, current_date, days_old", [ 
    ('1999-02-23', '2025-01-21', 9464),
    ('1970-01-01', '2025-01-21', 20109),
    ('2008-02-28', '2012-02-28', 1461),
    ('2008-02-28', '2012-02-29', 1462),
    ('2008-02-29', '2025-01-21', 6171),
    ('2008-02-28', '2025-01-21', 6172),
    ('2025-01-20', '2025-01-21', 1),
    ('2009-02-28', '2013-02-28', 1461),
    ('1996-09-23', '2025-01-23', 10349),
    ('1970-01-01', '2000-01-01', 10957)
])

def test_seasons(date_of_birth, current_date, days_old):
    assert seasons(date_of_birth=date_of_birth, current_date=current_date) == days_old


@pytest.mark.parametrize("days, minutes_in_words", [
    (9464, 'thirteen million, six hundred twenty-eight thousand, one hundred sixty minutes'),
    (20109, 'twenty-eight million, nine hundred fifty-six thousand, nine hundred sixty minutes'),
    (1462, 'two million, one hundred five thousand, two hundred eighty minutes'),
    (6171, 'eight million, eight hundred eighty-six thousand, two hundred forty minutes'),
    (6172, 'eight million, eight hundred eighty-seven thousand, six hundred eighty minutes'),
    (1, 'one thousand, four hundred forty minutes'),
    (10957, 'fifteen million, seven hundred seventy-eight thousand eighty minutes')
])

def test_days_to_minutes(days, minutes_in_words):
    assert days_to_minutes(days=days) == minutes_in_words


@pytest.mark.parametrize("user_input, date_of_birth",[
    ('I was born in 2005-11-30', '2005-11-30'),
    ('1999-12-31', '1999-12-31'),
    ('2008-02-29 2010-01-24', '2008-02-29'),
    ('1998-12-31', '1998-12-31'),
    ('2000-11-30', '2000-11-30'),
    ('2001-10-31', '2001-10-31'),
    ('2002-04-28', '2002-04-28'),
    ('2004-02-28', '2004-02-28')
])
def test_get_date_of_birth(user_input, date_of_birth):
    assert get_date(user_input) == date_of_birth

def test_get_date_with_invalid_date():
    with pytest.raises(ValueError):
        get_date('19999-01-23')
    with pytest.raises(ValueError):
        get_date('2005/01/24')
    with pytest.raises(ValueError):
        get_date('24/01/2000')
    with pytest.raises(ValueError):
        get_date("January, 1 2000")
    with pytest.raises(ValueError):
        get_date('1999/01/24')
    with pytest.raises(ValueError):
        get_date('2001-02-30')