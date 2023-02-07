# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# See proyect >> https://github.com/14wual/me
# Follow me >> https://twitter.com/codewual

#UNDER DEVELOPMENT

# --------------------Extern Imports--------------------
from datetime import datetime
import csv

# --------------------APP--------------------
class Tasks:
    
    def today():pass
    def _list():

        filename = "/usr/local/etc/me/local/share/csv/task.csv"
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['status'] == 'in time' or row['status'] == 'True' :
                    print(f"""
Title: {row[2]}""")

    def done():pass
    
    def add():
        
        now = datetime.now()
        
        formatted_time = now.strftime('%Y-%m-%d %H:%M:%S')
        title = input("Title: ")
        while title == "":title = input("Title: ")
        
        desc = input("[] Description: ")
        
        confirm1  = input("[N/y] You want to add an end date?: ")
        if confirm1 == "Y" or confirm1 == "y":
            while True:
                try:
                    date_string = input("Enter a date and time in the format %Y-%m-%d %H:%M:%S: ")
                    date_format = "%Y-%m-%d %H:%M:%S"
                    datetime_object = datetime.datetime.strptime(date_string, date_format)
                    break
                except:date_string = input("Enter a date and time in the format %Y-%m-%d %H:%M:%S: ")
                finally:status = 'in time'
        else:
            date_string = 'none'
            status = 'True'
        
        data = [formatted_time, date_string, title, desc, status]

        with open('/usr/local/etc/me/local/share/csv/task.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow(data)

