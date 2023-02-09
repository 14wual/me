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

# --------------------FUNCTIONALITIES--------------------
from _functs.password import Passwd
from _functs.notes import Notes
from _functs.browser import Browser
from _functs.check import Check
from _functs.pc import PC
from _functs.contacts import Modify, Add, Search

# --------------------COMMANDS--------------------
from _app.commands import DoBrowser
from _app.commands import DoCheck
from _app.commands import DoContacts
from _app.commands import DoMail
from _app.commands import DoNotes
from _app.commands import DoOther
from _app.commands import DoPassword
from _app.commands import DoPc
from _app.commands import DoPython
from _app.commands import DoTask

# --------------------MAIN--------------------
from _app.commands import MeAPP

# --------------------APP--------------------
if __name__ == '__main__':
    app = MeAPP()
    app.cmdloop()
