# Seasons of Love #

## Problem statement ##

Given a birth date in the format YYYY-MM-DD, find how old a person is in minutes to the nearest integer and Format the minutes to words without using and in between the words.

## Assumptions ##

1. User was born at midnight.

2. Current time is also midnight.

## Input ##

Date of birth i.e 1999-01-01.

## Output ##

Seconds in words from date of birth to today i.e Five hundered twenty-five thousand, six hundred minutes for above date

# Test #

## Cases ##

1. Date of birth in incorrect format i.e DD-MM-YYYY or MM-DD-YYY

2. A user 30 yrs old.

3.  A user 1  month old.

4. A user a day old.

5. A user 3 yrs old.

6. Current year is leap.

7. A user born in a leap year.

8. User born on Feb 29.

9. User born on Feb 28.

10. Date of birth in correct format YYY-MM-DD

tests = [

    {
        'input': 
        {

            'date_of_birth': '2008-02-28',
            'todays_date': '2012-02-28'
        },

        'output': 'five hundred twenty-five thousand, six hundred minutes'
    },

    {
        'input':
        {

            'date_of_birth': '1999-12-31',
            'todays_date': '2000-01-01'
        },

        'output': 'one thousand, four hundred forty minutes'
    },

    {
        'input': 
        {
            'date_of_birth': '1999-02-23',
            'todays_date': '2025-01-21'
        },

        'output': 'thirteen million, six hundred twenty-eight thousand, one hundred sixty minutes'

    },
    
     {
        'input': 
        {
            'date_of_birth': '1970-01-01',
            'todays_date': '2025-01-21'
        },

        'output': 'twenty-eight million, nine hundred fifty-six thousand, nine hundred sixty minutes'

    },

    {
        'input': 
        {
            'date_of_birth': '2008-02-28',
            'todays_date': '2012-02-28'
        },

        'output': 'two million, one hundred three thousand, eight hundred forty minutes'

    },


]




