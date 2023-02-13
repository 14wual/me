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
path = '/usr/local/etc/me/bin/me/me.ini'
with open(path, 'w') as f:f.close()
config.read(path)

config.add_section('software')
config.add_section('me')
config.add_section('databases')

config.set('me', 'version', '1.83')
config.set('me', 'user', user)
password = input("Write a Password: ")
config.set('me', 'password', password)

path = '/usr/local/etc/me/usr/txt/log/notes_inputs.csv'
config.set('me', 'notes', path)
path = '/usr/local/etc/me/usr/browser/log/favorites.csv'
config.set('me', 'browser', path)
path = '/usr/local/etc/me/local/share/database/password.db'
config.set('me', 'password', path)

config.set('software', 'browser', 'default')

with open("/usr/local/etc/me/bin/me/me.ini", "w") as config_file:config.write(config_file)

path = '/usr/local/etc/me/local/share/database/password.db' % user

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

notes_inputs_path = '/usr/local/etc/me/usr/txt/log/notes_inputs.csv'
favorites_path = '/usr/local/etc/me/usr/browser/log/favorites.csv'
task_path = '/usr/local/etc/me/local/share/csv/task.csv'

with open(notes_inputs_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['now', 'title'])

with open(favorites_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'site'])

with open(task_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['now', 'for', 'title', 'desc'])
    
ddbb_file_path = '/usr/local/etc/me/local/share/database/contacts.db'
conn = sqlite3.connect(ddbb_file_path)
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    surname TEXT,
    nickname TEXT,
    phone TEXT,
    mail TEXT,
    company TEXT,
    old_companies TEXT,
    web TEXT,
    tags TEXT,
    other TEXT
)
''')
conn.commit()
conn.close()
