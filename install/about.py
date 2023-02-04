# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# See proyect >> https://github.com/14wual/me
# Follow me >> https://twitter.com/codewual

import configparser
import os

config = configparser.ConfigParser()       
path = '/home/%s/.config/me/bin/me/me.ini' % os.environ['USER']
with open(path, 'w') as f:f.close
config.read(path)

config.add_section('software')
config.add_section('me')
config.add_section('databases')

config.set('me', 'version', '0.1')
user = input("Write a User ")
config.set('me', 'user', user)
password = input("Write a Password: ")
config.set('me', 'password', password)

path = '/home/%s/.config/me/usr/txt/log/notes_inputs.csv' % os.environ['USER']
config.set('me', 'notes', path)
path = '/home/%s/.config/me/usr/browser/log/favorites.csv' % os.environ['USER']
config.set('me', 'browser', path)
path = '/home/%s/.config/me/local/share/database/password.db' % os.environ['USER']
config.set('me', 'password', path)

config.set('software', 'browser', 'default')
