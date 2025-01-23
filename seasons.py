from sys import exit
import inflect
from datetime import date
from re import search, IGNORECASE

words = inflect.engine()

def seasons(date_of_birth: str, current_date: str)-> int:
    date_of_birth = date.fromisoformat(date_of_birth)
    current_date = date.fromisoformat(current_date)
    
    days_old = current_date - date_of_birth
    return days_old.days
    
def days_to_minutes(days: int)-> str:
    
    minutes = days * 1440

    return words.number_to_words(minutes, andword="") + " "+ words.plural('minute', minutes)

def get_date(date_of_birth: str)-> str|ValueError:
    pattern = r'\b(?P<date_of_birth>([0-9]{4}-(?:[0][13578]|10|12)-(?:[0][1-9]|[1-2][0-9]|[3][0-1]))|([0-9]{4}-02-(?:[0][0-9]|[1-2][0-9]))|([0-9]{4}-(?:[0][469]|11)-(?:[0][01-9]|[1-2][0-9]|[3][0-1])))\b'

    date = search(pattern=pattern, string=date_of_birth, flags=IGNORECASE)
    if date:
        return date.group('date_of_birth')
    raise ValueError


def main()->None:
    #d_o_b = "Hello, I was born in 1999/02/28"
    current_date = date.today()
    birth_day = input("Date of Birth: ")
    
    try:
        date_of_birth = get_date(birth_day)
    
    except ValueError:
        exit("Invalid date")
    else:
        pass
        # seasons(date_of_birth = date_of_birth, current_date=current_date)


if __name__ == "__main__":
    main()
