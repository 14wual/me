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
    import sys
    import signal
    import getpass
    import os
except ImportError: raise ImportError("Failed to import modules. Make sure it is installed correctly and is in the PYTHONPATH.")

# --------------------Intern Imports--------------------
from _app import commands  
    
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
        
        self.browser = commands.DoBrowser(self)
        self.python = commands.DoPython(self)
        self.mail = commands.DoMail(self)
        self.check = commands.DoCheck(self)
        self.contacts = commands.DoContacts(self)
        self.notes = commands.DoNotes(self)
        self.pc = commands.DoPc(self)
        self.password = commands.DoPassword(self)
        self.other = commands.DoOther(self)
        self.task = commands.DoTask(self)
        
        self.other.do_hello(line='')
        
    def default(self, line):
        try:super().default(line)
        except Exception as e:self.do_help()
        
    def do_passwd(self, line):self.password.do_passwd(line)
    def do_password(self, line):self.password.do_passwd(line)
    def do_p(self, line):self.password.do_passwd(line)
    def do_mail(self, line):self.mail.do_mail(line)
    def do_python(self, line):self.python.do_python(line)
    def do_py(self, line):self.python.do_python(line)
    def do_search(self, line):self.browser.do_search(line)
    def do_s(self, line):self.browser.do_search(line)
    def do_browser(self, line):self.browser.do_browser(line)
    def do_brow(self, line):self.browser.do_browser(line)
    def do_b(self, line):self.browser.do_browser(line)
    def do_check(self, line):self.check.do_check(line)
    def do_contacts(self, line):self.contacts.do_contacts(line)
    def do_c(self, line):self.contacts.do_contacts(line)
    def do_cont(self, line):self.contacts.do_contacts(line)
    def do_notes(self, line):self.notes.do_notes(line)
    def do_pc(self, line):self.pc.do_pc(line)
    def to_task(self, line):self.task.do_tasks(line)
    def to_t(self, line):self.task.do_tasks(line)
    def do_clear(self, line):os.system("clear")
    def do_cls(self, line):os.system("clear")
    def do_exit(self, line):return True
    def do_bye(self, line):return True
    def do_hi(self, line):self.other.do_hello(line)
    def do_hello(self, line):self.other.do_hello(line)
    def do_info(self, line):self.other.do_info(line)
    def do_i(self, line):self.other.do_info(line)
    def do_help(self, line):self.other.do_help(line)
    def do_h(self, line):self.other.do_help(line)
    
    def check_access():
        
        config = configparser.ConfigParser()
        config.read('/usr/local/etc/me/bin/me/me.ini')

        password = getpass.getpass(prompt='[] Password: ')    
        if password == config.get("me", "password"):return True
        else: return False
    
    