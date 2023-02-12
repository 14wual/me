# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# See proyect >> https://github.com/14wual/me
# Follow me >> https://twitter.com/codewual

# --------------------Extern Imports--------------------
import platform
import os
import configparser

# --------------------APP--------------------
class Save:

    def __init__(self, files):       
        self.Files = files
        self.conf_configparser = configparser.ConfigParser()
        self.conf_configparser.read('/usr/local/etc/me/bin/me/me.ini')
        
    def getSaved(self):
        
        saved_1 = self.conf_configparser.get('save', '0')
        saved_2 = self.conf_configparser.get('save', '1')
        saved_3 = self.conf_configparser.get('save', '2')
        
        self.saved_list = [saved_1, saved_2, saved_3]
        return self.saved_list
    
    def printSaved(self):
        for i, path_save in enumerate(Save.getSaved(self)):
            print(f"{i}. {path_save}")
            
    def selectSaved(self):
        
        Save.printSaved(self)
        
        while True:
            choice = input("Choose a number between 0 and 2: ")
            if choice.isdigit():
                choice = int(choice)
                if 0 <= choice <= 2:break
            print("Invalid input. Please enter a number between 0 and 2.")

        return choice
    
    def modifySaved(self, new_path):
        
        selected_path = Save.selectSaved(self)
        self.conf_configparser.set('save', f'{selected_path}', new_path)
        with open(self.ini_file_path, "w") as config_file:self.conf_configparser.write(config_file)

    def save_path(self, line):
        
        Save.getSaved(self)
        
        if len(line) == 0:new_path = Checks.getCurrentPath()
        else:
            check = Checks.check_str_path(line)
            if check == True:new_path = line
            else:print("The path is not valid.")
        
        for selected_path, item in enumerate(self.saved_list):
            if item == '' or not item or item == "":
                self.conf_configparser.set('save', f'{selected_path}', new_path)
                with open(self.ini_file_path, "w") as config_file:self.conf_configparser.write(config_file)
                break
            else:Save.modifySaved(self, new_path=new_path);break
            
class Checks:
    
    def __init__(self, files):self.Files = files
    def getCurrentPath():return Checks.replacePath(os.getcwd())
    def replacePath(current_path):return current_path.replace("\\", "/")
    def getOS():return platform.system()
    
    def check_str_path(path):
        if os.path.isabs(path):return True
        else:return False
    
    def getHomePath():
        if Checks.getOS() == 'Windows':return os.chdir(os.path.expandvars("%USERPROFILE%"))
        if Checks.getOS() == 'Linux':return os.chdir(os.path.expanduser("~"))
        else:print(f"Error{Checks.getOS()}: Not a supported operating system ")
