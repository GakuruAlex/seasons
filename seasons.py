from sys import exit
from datetime import datetime
from re import search, IGNORECASE
def seasons(date_of_birth: datetime, current_date: datetime)-> int:
    return 1
def days_to_minutes(days: int)-> str:
    return 1

def get_date(date_of_birth: str)-> str:
    pattern = r'\b(?P<date_of_birth>([0-9]{4}-(?:[0][13578]|10|12)-(?:[0][1-9]|[1-2][0-9]|[3][0-1]))|([0-9]{4}-02-(?:[0][0-9]|[1-2][0-9]))|([0-9]{4}-(?:[469]|11)-(?:[0][01-9]|[1-2][0-9]|[3][0-1])))\b'

    if (date := search(pattern=pattern, string=date_of_birth, flags=IGNORECASE)):
        return date.group('date_of_birth')
    raise ValueError


def main()->None:
    #d_o_b = "Hello, I was born in 1999/02/28"

    try:
        date_of_birth = get_date(input("Date of Birth: ")).group('date_of_birth')
    except ValueError:
        exit("Invalid date")
    else:
        print(date_of_birth)


if __name__ == "__main__":
    main()
