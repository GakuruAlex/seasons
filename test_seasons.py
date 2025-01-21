import pytest
from seasons import days_to_minutes, seasons


@pytest.mark.parametrize("date_of_birth, current_date, days_old",[ 
    ('1999-02-23', '2025-01-21', '9464'),
    ('1970-01-01', '2025-01-21', '20109'),
    ('2008-02-28', '2012-02-28', '1461'),
    ('2008-02-28', '2012-02-29', '1462'),
    ('2008-02-29', '2025-01-21', '6171'),
    ('2008-02-28', '2025-01-21', '6172'),
    ('2025-01-20', '2025-01-21', '1'),
    ('2009-02-28', '2013-02-28', '1461'),
    ('1/1/1970', '1/1/2000', '10957')
])

def test_seasons(date_of_birth, current_date, days_old):
    assert seasons(date_of_birth=date_of_birth, current_date=current_date) == days_old
