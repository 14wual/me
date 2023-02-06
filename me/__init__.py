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
    import signal
    import smtplib
except ImportError: raise ImportError("Failed to import modules. Make sure it is installed correctly and is in the PYTHONPATH.")

# --------------------Intern Imports--------------------
from _functs.password import Passwd
from _functs.notes import Notes
from _functs.browser import Browser
from _functs.check import Check
from _functs.pc import PC
from _functs.contacts import Modify, Add, Search

# --------------------APP--------------------
class MeAPP(cmd.Cmd):
    
    def handle_interrupt(signum, frame):
        print("Type [exit] or [bye] to exit!\nMore help with command [help].")
    
    signal.signal(signal.SIGINT, handle_interrupt)
    prompt = '<me> '
    
    def __init__(self, completekey='tab', stdin=sys.stdin, stdout=sys.stdout):
        super().__init__(completekey=completekey, stdin=stdin, stdout=stdout)
        
        now = datetime.now()
        MeAPP.formatted_time = now.strftime('%Y-%m-%d %H:%M:%S')
        
        self.config = configparser.ConfigParser()
        self.config.read('/usr/local/etc/me/bin/me/me.ini')

        self.do_hello(line='')
        
    def do_mail(self, line):
        
        print("In order to use this service;\n"
      "    your google account must have 'access to less secure apps' enabled.\n\n"
      "Read more:\n"
      "https://support.google.com/mail/answer/7126229?visit_id=638113077287409177-2088778801&p=BadCredentials&rd=2#cantsignin&zippy=%2I-can't-start-session%C3%B3n-in-my-mail-client")
        
        config = configparser.ConfigParser()
        config.read('/usr/local/etc/me/bin/me/me.ini')
        
        ant = config.get("software", "mail")
        
        sender_email = input(f"[{ant}] Write your mail: ")
        if not sender_email:sender_email = ant
        config.set("databases", "mail", sender_email)
        try:
            with open("/usr/local/etc/me/bin/me/me.ini", "w") as config_file:config.write(config_file)
        except:pass
        
        print("The password will not be saved.")
        password = input("Write your mail-password: ")
        receiver_email = input("Write your recipient email: ")
        subject = input("Write a subjet: ")
        message = input("Write the mail: ")
        
        showpasswd = len(password)*"*"
        print(f"""
Mail from: {sender_email}
Your Mail Password: {showpasswd}
Mail to: {receiver_email}

Subjet: {subject}
Message: {message}
              """)
        
        confirm = input("[N/y]It's right?: ")
        if confirm == "":confirm="N"
        
        if confirm == "Y" or confirm == "y":
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.ehlo()
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
        
    def do_py(self, line):self.do_python(line='')
    def do_python(self,line):
        print("[exit()] to exit py terminal.")
        while True:
            try:cm = exec(input("<py> "))
            except:pass
            if cm == "exit()":break
            if cm == "":break
        
    def do_browser(self, line):
        
        parser = argparse.ArgumentParser(description='BRowser Commands')
        
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
            
    def do_check(self, line):
        
        parser = argparse.ArgumentParser(description='Check Commands')
        
        parser.add_argument('--connect', dest='connect', action='store_true', help='ACheck connectivity with a web or ip.')
        parser.add_argument('--file', dest='file', action='store_true', help='Check if a directory exists.')
        parser.add_argument('--path', dest='path', action='store_true', help=' Ceck if a file exists.')
        parser.add_argument('-w', type=str, help=' write the directory, url, ... (string)')

        args = parser.parse_args(line.split())
        
        if not args.w:
            dire = input("Write: ")
        else: dire = args.w
        
        if args.connect:Check.connect(dire)
        elif args.file:Check.files(dire)
        elif args.path:Check.path(dire)
        else:
            print("ArgsError: the 'check' command needs arguments | [--connect] [--file] [--path]")
        
    def do_search(self, line):
                
        search_term = input("Your Search Value: ")        
        url = "https://www.google.com/search?q=" + search_term
        MeAPP.open_browser(url)
        
    def open_browser(url):subprocess.Popen(["xdg-open", url])
        
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
        
    def do_pc(self, line):
        
        parser = argparse.ArgumentParser(description='PC Commands')
        parser.add_argument('--all', dest='all', action='store_true', help='Print all logs')
        parser.add_argument('--ram', dest='ram', action='store_true', help='Current status of: ram')
        parser.add_argument('--cpu', dest='cpu', action='store_true', help='Current status of: cpu')
        parser.add_argument('--disks', dest='disks', type=str, help='Current status of: disks')
        parser.add_argument('--processor', dest='processor', type=str, help='Current status of: processor')
        
        args = parser.parse_args(line.split())
        
        if args.all:PC.memory();PC.cpu();PC.disk();PC.processes()
        elif args.ram:PC.memory()
        elif args.cpu:PC.cpu()
        elif args.disks:PC.disk()
        elif args.processor:PC.processes()
        else:
            print("ArgsError: the 'pc' command needs arguments | [--all] [--ram] [--cpu] [--disks] [--processes]")
            PC.memory();PC.cpu();PC.disk();PC.processes()
            
    def do_contacts(self, line):
        parser = argparse.ArgumentParser(description='Contacs Commands')
        
        parser.add_argument('--modify', dest='modify', action='store_true', help='Add New Key to Vault')
        parser.add_argument('--search', dest='search', action='store_true', help='Search & Copy Key from Vault')
        parser.add_argument('--add', dest='add', action='store_true', help='Import Keys from csv to Vault')
        parser.add_argument('--delete', dest='delete', type=str, help='Search & Modify Key from Vault ')
        
        args = parser.parse_args(line.split())
        
        if args.modify:
            value = input("Value: ")
            Modify.modify_contact(value)
        elif args.search:
            value = input("Value: ")
            Search.search_contact(value)
        elif args.delete:
            value = input("Value: ")
            Modify.delete_contact(value)
        elif args.add:Add.contact_info()
        else:print("ArgsError: the 'contacts' command needs arguments | [--add] [--delete] [--search] [--modify]")
        
    def default(self, line):
        try:super().default(line)
        except Exception as e:self.do_help()
        
    def do_hi(self, line):self.do_hello(line='')
    def do_clear(self, line):os.system("clear")
    def do_cls(self, line):os.system("clear")
    def do_exit(self, line):return True
    def do_bye(self, line):return True
    def do_hello(self, line):  
        print(f"""\n

                Welcome to Me! 
▒█▀▄▀█ ▒█▀▀▀    User: {self.config.get("me", "user")}
▒█▒█▒█ ▒█▀▀▀    Version: V.{self.config.get("me", "version")} 
▒█░░▒█ ▒█▄▄▄    Now: {MeAPP.formatted_time}
                (code by wual)

\n""")
    def do_info(self, line):print("""
Welcome to ME!
                                  
Version: BV0.63
File path: ~/.config/me

Code By WUAL >> https://github.com/14wual
Star: https://github.com/14wual/me
Twitter: https://twitter.com/codewual

Powered by 14wual/me!
                                  """)
    def do_help(self, line):print("""Browser Commands:
    browser: search and browse bookmarks.
    browser --add: add a new bookmark.
    browser --delete: delete a new bookmark.
    browser --list: list your bookmarks.
    search: do a google search.

[mail]: Send an email.
    
[contacts] Contacts Commands:
    contacts --modify: look for a contact.
    contacts --search: modify an existing contact.
    contacts --add: add a new contact.
    contacts --delete: delete an existing contact.

[passwd] | Password Commands:
    passwd --add: Add New Key to Vault.
    passwd --copy: Search & Copy Key from Vault.
    passwd --matter: Import Keys from csv to Vault.
    passwd --modify: Search & Modify Key from Vault.
    
[notes] Notes Commands:
    notes --new: Create a new note.
    notes --read: View all notes, select one write/read.
    notes --delete: Delete a note.
    
[pc] PC Commands:
    pc --all: Print all logs
    pc --ram: Current status of: ram
    pc --cpu: Current status of: cpu
    pc --disks: Current status of: disks
    pc --processor: Current status of: processor

[check] Check Commands:
    check --connect: Check connectivity with a web or ip.
    check --path: Check if a directory exists.
    check --file: Ceck if a file exists.
    second options/optional: -w: write the directory, url, ... (string)
        check --command -w example
        
[python] or [py]: Create a python terminal.
    
Other Commands:
    clear/cls: clear terminal
    info: View app information
    hello/hi: Initial greeting of the app
    exit/bye: Exit the program""")

if __name__ == '__main__':
    MeAPP(completekey='tab').cmdloop()
