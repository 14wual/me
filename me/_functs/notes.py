# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# See proyect >> https://github.com/14wual/me
# Follow me >> https://twitter.com/codewual

# --------------------Extern Imports--------------------
try:    
    from datetime import datetime
    import os
    import configparser
    import csv
except ImportError: raise ImportError("Failed to import modules. Make sure it is installed correctly and is in the PYTHONPATH.")

# --------------------APP--------------------
class Notes:
    
    config = configparser.ConfigParser()
    config.read('/usr/local/etc/me/bin/me/me.ini')
    
    def new():
        
        now = datetime.now()
        formatted_time = now.strftime('%Y-%m-%d %H:%M:%S')
        
        title = input("[] Title: ")
        
        if title == "": title = f"note_{now.strftime('%Y-%m-%d_%H:%M:%S')}.txt"
        elif title != "": title = title+".txt"
        
        confirm = input("[Y/n] It's right?: ")
        if confirm == "":confirm="Y"
        
        path = os.path.join("/usr/local/etc/me/usr/txt" % os.environ['USER'], title) 
        
        row = [
            [f"{formatted_time}", f"{title}"]
        ]
        csv_path = Notes.config.get("databases", "notes")
        with open(csv_path, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(row)
        
        if confirm == "Y" or confirm == "y":
                os.system(f'nano {path}')
            
    def read():

        path = "/usr/local/etc/me/usr/txt"

        files = [file for file in os.listdir(path) if file.endswith(".txt")]
        
        total = Notes.count_txt_files(path)

        print("Your Notes:")
        for i, file in enumerate(files, 1):
            print("{}. {}".format(i, file))
            if (i % 5 == 0):input(f"[{total}] Press Enter to continue...")


        selection = int(input("Select a file by its number: "))
        if selection < 1 or selection > len(files):print("Invalid selection.")
        else:
            selected_file = files[selection - 1]
            os.system("nano {}/{}".format(path, selected_file))    
        
    def count_txt_files(ruta):
        counter = 0
        for file in os.listdir(ruta):
            if file.endswith(".txt"):
                counter += 1
        return counter
        
    def archive():
        
        path = "/usr/local/etc/me/usr/txt/archive"

        files = [file for file in os.listdir(path) if file.endswith(".txt")]
        
        total = Notes.count_txt_files(path)

        print("Your Notes:")
        for i, file in enumerate(files, 1):
            print("{}. {}".format(i, file))
            if (i % 5 == 0):input(f"[{total}] Press Enter to continue...")


        selection = int(input("Select a file by its number: "))
        if selection < 1 or selection > len(files):print("Invalid selection.")
        else:
            selected_file = files[selection - 1]
            os.system("nano {}/{}".format(path, selected_file))
        
    def delete():
        
        path = "/usr/local/etc/me/usr/txt/"

        files = [file for file in os.listdir(path) if file.endswith(".txt")]
        
        total = Notes.count_txt_files(path)

        print("Your Notes:")
        for i, file in enumerate(files, 1):
            print("{}. {}".format(i, file))
            if (i % 5 == 0):input(f"[{total}] Press Enter to continue...")


        selection = int(input("Select a file by its number: "))
        if selection == "": selection = 1
        if selection < 1 or selection > len(files):print("Invalid selection.")
        else:
            selected_file = files[selection - 1]
            os.system("rm {}/{}".format(path, selected_file))
        
            print(f"Deleted: {selected_file}")
