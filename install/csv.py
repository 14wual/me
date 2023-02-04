# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# See proyect >> https://github.com/14wual/me
# Follow me >> https://twitter.com/codewual

import csv
import os

user  = input("User: ")
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
