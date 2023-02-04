# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# See proyect >> https://github.com/14wual/me
# Follow me >> https://twitter.com/codewual

# --------------------Extern Imports--------------------
import webbrowser
import csv
import os
import configparser

# --------------------APP--------------------
class Browser:
    
    config = configparser.ConfigParser()
    config.read('/home/%s/.config/me/bin/me/me.ini' % os.environ['USER'])

    def add():
        
        name = input("Name: ")
        print("For the proper functioning of URLs, write the full url | Example https://github.com/14wual")
        url = input("url: ")
        
        confirm = input("[y/N] The data is ok?: ")
        if confirm == "Y" or confirm == "y":
            Browser.add_row(name, url)
            print(f"{name} Added!")                
        else:pass
        
    def add_row(name, url):
        with open(Browser.config.get("databases", "browser"), 'a') as f:
            writer = csv.writer(f)
            writer.writerow([name, url])
        
    def delete():
        
        path = Browser.config.get("databases", "browser")
        with open(path, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            rows = list(reader)
            while True:
                for i, row in enumerate(rows):
                    print(f"{i + 1}. Name: {row[0]} | URL: {row[1]}")
                try:
                    choice = int(input("Choose a number to delete the specific row: "))
                    if 1 <= choice <= len(rows):
                        del rows[choice - 1]
                        break
                    else:
                        print("Invalid number. Try again.")
                except ValueError:
                    print("Invalid input. Try again.")
        
        with open(path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(rows)

    
    def lists():
        path = Browser.config.get("databases", "browser")
        with open(path, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for i, row in enumerate(reader):
                try:print(f"{i + 1}. Name: {row[0]} | URL: {row[1]}")
                except:pass
    
    def search():
    
        path = Browser.config.get("databases", "browser")
        with open(path, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            rows = list(reader)
            while True:
                for i, row in enumerate(rows):
                    print(f"{i + 1}. Name: {row[0]} | URL: {row[1]}")
                try:
                    choice = int(input("Choose a number to see the specific row: "))
                    if 1 <= choice <= len(rows):
                        break
                    else:
                        print("Invalid number. Try again.")
                except ValueError:
                    print("Invalid input. Try again.")

        webbrowser.open_new_tab(row[1])
