# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# See proyect >> https://github.com/14wual/me
# Follow me >> https://twitter.com/codewual

# --------------------Extern Imports--------------------
from datetime import datetime
import os
import csv

# --------------------APP--------------------
class Tasks:
    
    def today():
        
        today = datetime.now().strftime('%Y-%m-%d')
        filename = "/usr/local/etc/me/local/share/csv/task.csv"
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['for'] == today:
                    print(f"Task found for today: {row['title']}")
                    return True
        print("No task found for today.")
        return False
        
    def _list():
        
        filename = "/usr/local/etc/me/local/share/csv/task.csv"
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            tasks = list(reader)
            for i, task in enumerate(tasks):
                if task['status'] == 'in time' or task['status'] == 'True':print(f"Task {i+1}: {task['title']}")

        num = int(input("Enter the task number to see more details: "))
        task = tasks[num - 1]
        print(f"""
Task: {num}
Title: {task['title']}
Description: {task['desc']}
Finished: {task['for']}
Status: {task['status']}
              """)

    def done():
        
        filename = "/usr/local/etc/me/local/share/csv/task.csv"
        temp_file = "/usr/local/etc/me/local/share/csv/temp.csv"
        
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            tasks = list(reader)
            for i, task in enumerate(tasks):
                if task['status'] == 'in time' or task['status'] == 'True':print(f"Task {i+1}: {task['title']}")
        
        task_number = int(input("Enter the task number to mark as done: "))
        task_count = 0

        with open(filename, 'r') as file, open(temp_file, 'w') as temp:
            reader = csv.DictReader(file)
            writer = csv.DictWriter(temp, fieldnames=reader.fieldnames)
            writer.writeheader()

            for row in reader:
                task_count += 1
                if task_count == task_number:
                    row['status'] = 'done'
                writer.writerow(row)

        os.remove(filename)
        os.rename(temp_file, filename)
        
        print("Marked as done.")

    
    def add():
        
        now = datetime.now()
        
        formatted_time = now.strftime('%Y-%m-%d')
        title = input("Title: ")
        while title == "":title = input("Title: ")
        
        desc = input("[] Description: ")
        
        confirm1  = input("[N/y] You want to add an end date?: ")
        if confirm1 == "Y" or confirm1 == "y":
            while True:
                try:
                    date_string = input("Enter a date and time in the format %Y-%m-%d ")
                    date_format = "%Y-%m-%d"
                    datetime_object = datetime
                    datetime.strptime(date_string, date_format)
                    break
                except:date_string = input("Enter a date and time in the format %Y-%m-%d2: ")
                finally:status = 'in time'
        else:
            date_string = 'none'
            status = 'True'
        
        data = [formatted_time, date_string, title, desc, status]

        with open('/usr/local/etc/me/local/share/csv/task.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow(data)

