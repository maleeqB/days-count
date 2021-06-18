from datetime import datetime
import sys
import textwrap
from dob import calc_dates


def get_welcome_text():
    welcome_text = textwrap.dedent("""\
    DOB : print total days since day of Birth
    python3 [dob_cli.py] [day] [month] [year] 
    By: AbdulMalik Bello\
    """)
    return welcome_text


def get_user_birthday():
    if len(sys.argv) < 4:
        print("\nERROR: Three Command line arguments required")
        sys.exit(1)
    if invalid_argument():
        print("\nERROR: Only Integer arguments are supported")
        sys.exit(1)
    day, month, year = get_arguments()
    return datetime(year, month, day)


def get_arguments():
    return int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])


def invalid_argument():
    invalid_arg = False
    for i in range(1, 4):
        if not sys.argv[i].isdigit():
            invalid_arg = True
    return invalid_arg


if __name__ == "__main__":
    print(get_welcome_text())
    birthday = get_user_birthday()
    now = datetime.now()
    total_days, next_birthday = calc_dates(birthday, now)
    print(textwrap.dedent("""
        Total days: %s
        Next birthday is: %s    
        """) % (total_days, next_birthday))
