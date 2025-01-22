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
    ('1/1/1970', '1/1/2000', 10957)
])

def test_seasons(date_of_birth, current_date, days_old):
    assert seasons(date_of_birth=date_of_birth, current_date=current_date) == days_old


@pytest.mark.parametrize("days, minutes_in_words", [
    (9464, 'nine thousand, four hundred sixty-four minutes'),
    (20109, 'twenty thousand, one hundred nine minutes'),
    (1462, 'one thousand, four hundred sixty-two minutes'),
    (6171, 'six thousand, one hundred seventy-one minutes'),
    (6172, 'six thousand, one hundred seventy-two minutes'),
    (1, 'one minute'),
    (10957, 'ten thousand, nine hundred fifty-seven minutes')
])

def test_days_to_minutes(days, minutes_in_words):
    assert days_to_minutes(days=days) == minutes_in_words


@pytest.mark.parametrize("user_input, date_of_birth",[
    ('I was born in 2005-11-30', '2005-11-30'),
    ('1999-12-31', '1999-12-31'),
    ('2008-02-29 2010-01-24', '2008-02-29')
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