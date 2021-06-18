import textwrap
from datetime import datetime


def get_welcome_text():
    welcome_text = textwrap.dedent("""
            print total days since day of Birth, and next birthday

            day : Day of Birth
            month : Month of Birth
            year : Year Of Birth

            e.g user given birth to on 2nd August 2001 has the following values
            day: 2
            month: 8
            year: 2001

            By: AbdulMalik Bello
            """)
    return welcome_text


def get_user_birthday():
    day = get_int_input("Enter day ")
    month = get_int_input("Enter month ")
    year = get_int_input("Enter Year ")
    return datetime(year, month, day)


def calc_dates(birthday, now):

    delta1 = datetime(now.year, birthday.month, birthday.day)
    delta2 = datetime(now.year + 1, birthday.month, birthday.day)

    total_days = now - birthday
    next_birthday = (delta1 if delta1 > now else delta2) - now

    return total_days, next_birthday


def get_int_input(msg):
    user_input = ""
    done = False
    while not done:
        inp = input(msg)
        if inp.isdecimal():
            user_input = inp
            done = True
        else:
            print("Please Enter digits only")
    return int(user_input)


if __name__ == "__main__":
    print(get_welcome_text())
    birthday = get_user_birthday()
    now = datetime.now()
    total_days, next_birthday = calc_dates(birthday, now)
    print(textwrap.dedent("""
    Total days: %s
    Next birthday is: %s    
    """) % (total_days, next_birthday))
