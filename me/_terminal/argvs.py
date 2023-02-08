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
    import sys
    import os
except ImportError: raise ImportError("Failed to import modules. Make sure it is installed correctly and is in the PYTHONPATH.")

# --------------------APP--------------------
class CheckArgsv:
    
    def check_argvs(self):
        
        line = ''
    
        if len(sys.argv) > 1:

            if len(sys.argv) > 2:line =  sys.argv[2]
            else:line == ''
            
            if sys.argv[1] == 'passwd':self.password.do_passwd(line)
            elif sys.argv[1] == 'password':self.password.do_passwd(line)
            elif sys.argv[1] == 'p':self.password.do_passwd(line)
            elif sys.argv[1] == 'mail':self.mail.do_mail(line)
            elif sys.argv[1] == 'python':self.python.do_python(line)
            elif sys.argv[1] == 'py':self.python.do_python(line)
            elif sys.argv[1] == 'search':self.browser.do_search(line)
            elif sys.argv[1] == 's':self.browser.do_search(line)
            elif sys.argv[1] == 'browser':self.browser.do_browser(line)
            elif sys.argv[1] == 'brow':self.browser.do_browser(line)
            elif sys.argv[1] == 'b':self.browser.do_browser(line)
            elif sys.argv[1] == 'check':self.check.do_check(line)
            elif sys.argv[1] == 'contacts':self.contacts.do_contacts(line)
            elif sys.argv[1] == 'c':self.contacts.do_contacts(line)
            elif sys.argv[1] == 'cont':self.contacts.do_contacts(line)
            elif sys.argv[1] == 'notes':self.notes.do_notes(line)
            elif sys.argv[1] == 'pc':self.pc.do_pc(line)
            elif sys.argv[1] == 'task':self.task.do_tasks(line)
            elif sys.argv[1] == 't':self.task.do_tasks(line)
            elif sys.argv[1] == 'hi':self.other.do_hello(line)
            elif sys.argv[1] == 'hello':self.other.do_hello(line)
            elif sys.argv[1] == 'info':self.other.do_info(line)
            elif sys.argv[1] == 'i':self.other.do_info(line)
            elif sys.argv[1] == 'help':self.other.do_help(line)
            elif sys.argv[1] == 'h':self.other.do_help(line)
        else:self.other.do_help(line)
              
    
