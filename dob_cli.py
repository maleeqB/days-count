import datetime
import sys


class Dob:
        	def __init__(self):
        		self.welcome_text = """DOB : print total days since day of Birth
        	
        	python3 [dob_cli.py] [day] [month] [year] 
        	
                By: AbdulMalik Bello
                """
        	def calc_dob(self):
        			if(len(sys.argv) < 4):
        				raise Exception("ERROR: Three Command line arguments required")
        			if(self.invalid_argument()):
        				raise Exception("ERROR: Only Integer arguments are supported") 
        				
        			day, month, year = self.get_arguments()
        			today = datetime.datetime.now()
        			birthday = datetime.datetime(year, month, day)
        			total_days = today - birthday
        			
        			return total_days
        			
        	def get_arguments(self):
        		return (int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
        	
        	def invalid_argument(self):
        		invalid_arg = False
        		for i in range(1,4):
        			if(not sys.argv[i].isdigit()): invalid_arg = True
        		return invalid_arg
        	
        	def __repr__(self):
        		print(self.welcome_text)
        		total_days = self.calc_dob()
        		return str(total_days)

if __name__ == "__main__":
    print(Dob())
    
