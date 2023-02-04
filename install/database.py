# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# See proyect >> https://github.com/14wual/me
# Follow me >> https://twitter.com/codewual

import sqlite3
import os

path = '/home/%s/.config/me/local/share/database/password.db' % os.environ['USER']

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
