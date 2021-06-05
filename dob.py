import datetime

class Dob:
    def __init__(self):
        self.welcome_text = """
        DOB : print total days since day of Birth

        day : Day of Birth
        month : Month of Birth
        year : Year Of Birth

        e.g user given birth to on 2nd August 2001 has the following values
        day: 2
        month: 8
        year: 2001

        By: AbdulMalik Bello
        """

    def calc_dob(self):
        day = self.get_input("Enter day ")
        month = self.get_input("Enter month ")
        year = self.get_input("Enter Year ")

        today = datetime.datetime.now()
        birthday = datetime.datetime(year, month, day)
        
        total_days = today - birthday
        return total_days


    def get_input(self, msg):
        user_input = ""
        done = False 
        while(not done):
            inp = input(msg)
            if inp.isdigit():
                user_input = inp
                done = True
            else: print("Please Enter digits only")
        return int(user_input)

    def __repr__(self):
        print(self.welcome_text)
        total_days = self.calc_dob()
        return str(total_days)


if __name__ == "__main__":
    print(Dob())
