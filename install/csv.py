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

notes_inputs_path = '/home/%s/.config/me/usr/txt/log/notes_inputs.csv' % os.environ['USER']
favorites_path = '/home/%s/.config/me/usr/browser/log/favorites.csv' % os.environ['USER']
task_path = '/home/%s/.config/me/local/share/csv/task.csv' % os.environ['USER']

with open(notes_inputs_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['now', 'title'])

with open(favorites_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'site'])

with open(task_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['now', 'for', 'title', 'desc'])
