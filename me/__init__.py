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
    import configparser
    import cmd
    from datetime import datetime
    import argparse
    import sys
    import os
    import getpass
    import subprocess
except ImportError: raise ImportError("Failed to import modules. Make sure it is installed correctly and is in the PYTHONPATH.")

# --------------------Intern Imports--------------------
from _functs.password import Passwd
from _functs.notes import Notes
from _functs.browser import Browser

# --------------------APP--------------------
class MeAPP(cmd.Cmd):
    
    prompt = '<me> '
    
    def __init__(self, completekey='tab', stdin=sys.stdin, stdout=sys.stdout):
        super().__init__(completekey=completekey, stdin=stdin, stdout=stdout)
        
        now = datetime.now()
        MeAPP.formatted_time = now.strftime('%Y-%m-%d %H:%M:%S')
        
        self.config = configparser.ConfigParser()
        self.config.read('/home/%s/.config/me/bin/me/me.ini' % os.environ['USER'])

        self.do_hello(line='')
        
    def do_browser(self, line):
        
        parser = argparse.ArgumentParser(description='Passwords Commands')
        
        parser.add_argument('--add', dest='add', action='store_true', help='Add New Favorite Site')
        parser.add_argument('--delete', dest='delete', action='store_true', help='Delete Favorite Site')
        parser.add_argument('--list', dest='list', action='store_true', help='Delete Favorite Site')
        
        args = parser.parse_args(line.split())
        
        if args.add:Browser.add()
        elif args.list:Browser.lists()
        elif args.delete:
            if self.check_access() == True:Browser.delete()
        else:
            Browser.search()
        
    def do_search(self, line):
                
        search_term = input("Your Search Value: ")        
        url = "https://www.google.com/search?q=" + search_term
        MeAPP.open_browser(url)
        
    def open_browser(url):
        subprocess.Popen(["xdg-open", url])
        
    def do_notes(self, line):
        
        parser = argparse.ArgumentParser(description='Notes Commands')
        
        parser.add_argument('--new', dest='new', action='store_true', help='Add/Create New Note')
        parser.add_argument('--read', dest='read', action='store_true', help='Read & Write Notes')
        parser.add_argument('--delete', dest='delete', action='store_true', help='Delete Notes')

        args = parser.parse_args(line.split())
        
        if args.new:Notes.new()
        elif args.read:Notes.read()
        elif args.delete:
            if self.check_access() == True:Notes.delete()
        else:
            print("ArgsError: the 'notes' command needs arguments | [--new] [--read] [--archive] [--delete]\nShowing notes")
            Notes.read()
            
        
    def do_passwd(self, line):
        
        parser = argparse.ArgumentParser(description='Passwords Commands')
        
        parser.add_argument('--add', dest='add', action='store_true', help='Add New Key to Vault')
        parser.add_argument('--copy', dest='copy', action='store_true', help='Search & Copy Key from Vault')
        parser.add_argument('--matter', dest='matter', action='store_true', help='Import Keys from csv to Vault')
        parser.add_argument('--delete', dest='delete', type=str, help='Search & Modify Key from Vault ')

        args = parser.parse_args(line.split())

        if self.check_access() == True:
            
            if args.copy:Passwd.copy()
            elif args.matter:Passwd.matter()
            elif args.delete:Passwd.modify()
            elif args.add:Passwd.add()
            else:print("ArgsError: the 'passwd' command needs arguments | [--add] [--copy] [--matter] [--modify]")
            
        else:print("Error: You must be login to run this command")
        
    def check_access(self):

        password = getpass.getpass(prompt='[] Password: ')
        
        if password == self.config.get("me", "password"):return True
        else: return False
            
        
        
    def do_hi(self, line):self.do_hello(line='')
    def do_clear(self, line):os.system("clear")
    def do_cls(self, line):os.system("clear")
    def do_exit(self, line):return True
    def do_bye(self, line):return True
    def do_hello(self, line):  
        print(f"""\n
Welcome to Me!
Version: V.{self.config.get("me", "version")}
Now: {MeAPP.formatted_time}
\n""")
    
    def do_help(self, line):print("""Browser Commands:
    browser:
    browser --add:
    browser --delete:
    browser --list: 
    search: 
     
[passwd] | Password Commands:
    passwd --add: Add New Key to Vault
    passwd --copy: Search & Copy Key from Vault
    passwd --matter: Import Keys from csv to Vault
    passwd --modify: Search & Modify Key from Vault
    
[notes] Notes Commands:
    notes --new: Create a new note
    notes --read: View all notes, select one write/read
    notes --delete: Delete a note
    
Other Commands:
    clear/cls: clear terminal
    info: View app information
    mypc: View current hardware/software status
    hello/hi: Initial greeting of the app
    exit/bye: Exit the program""")

if __name__ == '__main__':
    MeAPP(completekey='tab').cmdloop()