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
import sqlite3
import csv

user  = input("User: ")
config = configparser.ConfigParser()       
path = '/home/%s/.config/me/bin/me/me.ini' % user
with open(path, 'w') as f:f.close()
config.read(path)

config.add_section('software')
config.add_section('me')
config.add_section('databases')

config.set('me', 'version', '0.1')
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

path = '/home/%s/.config/me/local/share/database/password.db' % user

with open(path, 'w') as file:file.close()

print("[] Connecting to the ddbb...")
conn = sqlite3.connect(path)

try:cursor = conn.cursor()
finally:print("[ ✓ ] Established connection.")

print("[] Creating table, setting columns...")
cursor.execute('''
CREATE TABLE IF NOT EXISTS passwords (
    url TEXT,
    username TEXT,
    password TEXT,
    totp TEXT,
    extra TEXT,
    name TEXT,
    grouping TEXT,
    fav INTEGER
)
''')

try:
    conn.commit()
    print("[ ✓ ] Successfully configured.")
except sqlite3.OperationalError:print("[ ✕ ] Configuration failure.")

print("[] Closing connection...")
try:
    conn.close()
    print("[ ✓ ] Connection closed correctly")
except:print("[ ✕ ] Could not close the connection")

notes_inputs_path = '/home/%s/.config/me/usr/txt/log/notes_inputs.csv' % user
favorites_path = '/home/%s/.config/me/usr/browser/log/favorites.csv' % user
task_path = '/home/%s/.config/me/local/share/csv/task.csv' % user

with open(notes_inputs_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['now', 'title'])

with open(favorites_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'site'])

with open(task_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['now', 'for', 'title', 'desc'])
