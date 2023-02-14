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
from _terminal.argvs import CheckArgsv
from _functs.files import Checks
    
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
        self.files = commands.DoFiles(self)
        self.games = commands.DoGames(self)
        
        self.other.do_hello(line='')
        CheckArgsv.check_argvs(self)
        
    def emptyline(self):print("[help]? I think you should write something.") 
    def default(self, line):self.do_help(line)
        
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
    def do_task(self, line):self.task.do_tasks(line)
    def do_t(self, line):self.task.do_tasks(line)
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
    def do_games(self, line):self.games.view(line)
    def do_rps(self, line):self.games.do_rps(line)
    def do_gtn(self, line):self.games.do_gtn(line)
    
    def do_pwd(self, line):print(Checks.getCurrentPath())
    def do_cd(self, line):self.files.change_path(path=line)
    def do_save(self, line):self.files.save(line=line)
    def do_ls(self, line):self.files.do_ls(line=line)
    def do_cp(self, line):self.files.do_cp(line=line)
    def do_mv(self, line):self.files.do_mv(line=line)
    def do_view(self, line):self.files.do_view(line=line)
    def do_ren(self, line):self.files.do_ren(line=line)
    def do_rm(self, line):self.files.do_rm(line=line)
    def do_mkdir(self, line):self.files.do_mkdir(line=line)
    
    def complete_passwd(self, text, line, begidx, endidx):self.password.complete_passwd(text, line, begidx, endidx)
    def complete_password(self, text, line, begidx, endidx):self.password.complete_passwd(text, line, begidx, endidx)
    def complete_p(self, text, line, begidx, endidx):self.password.complete_passwd(text, line, begidx, endidx)
    def complete_search(self, text, line, begidx, endidx):self.browser.complete_search(text, line, begidx, endidx)
    def complete_s(self, text, line, begidx, endidx):self.browser.complete_search(text, line, begidx, endidx)
    def complete_browser(self, text, line, begidx, endidx):self.browser.complete_browser(text, line, begidx, endidx)
    def complete_brow(self, text, line, begidx, endidx):self.browser.complete_browser(text, line, begidx, endidx)
    def complete_b(self, text, line, begidx, endidx):self.browser.complete_browser(text, line, begidx, endidx)
    def complete_check(self, text, line, begidx, endidx):self.check.complete_check(text, line, begidx, endidx)
    def complete_contacts(self, text, line, begidx, endidx):self.contacts.complete_contacts(text, line, begidx, endidx)
    def complete_c(self, text, line, begidx, endidx):self.contacts.complete_contacts(text, line, begidx, endidx)
    def complete_cont(self, text, line, begidx, endidx):self.contacts.complete_contacts(text, line, begidx, endidx)
    def complete_notes(self, text, line, begidx, endidx):self.notes.complete_notes(text, line, begidx, endidx)
    def complete_pc(self, text, line, begidx, endidx):self.pc.complete_pc(text, line, begidx, endidx)
    def complete_task(self, text, line, begidx, endidx):self.task.complete_tasks(text, line, begidx, endidx)
    def complete_t(self, text, line, begidx, endidx):self.task.complete_tasks(text, line, begidx, endidx)

    def complete_cd(self, text, line, begidx, endidx):
        if not text:completions = os.listdir('.')
        else:completions = [f for f in os.listdir('.') if f.startswith(text)]
        return completions
    
    def check_access():
        
        config = configparser.ConfigParser()
        config.read('/usr/local/etc/me/bin/me/me.ini')

        password = getpass.getpass(prompt='[] Password: ')    
        if password == config.get("me", "password"):return True
        else: return False
