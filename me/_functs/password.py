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
    import pyperclip as clipboard
    from urllib.parse import urlparse
    import sqlite3
    import os
    import csv
    import random
except ImportError: raise ImportError("Failed to import modules. Make sure it is installed correctly and is in the PYTHONPATH.")

# --------------------APP--------------------
class Passwd:

    def matter():
        
        conn = sqlite3.connect('/usr/local/etc/me/local/share/database/password.db')
        cursor = conn.cursor()
        
        path = input("\nIt is recommended that the path be found in input\\*.csv. And that this is a relative path within the main folder.\n\n[input\*.csv] Write the path:")
        if path == "":path = r'*.csv'

        if os.path.exists(path):
            with open(path, 'r') as file:

                reader = csv.reader(file)
                next(reader)

                for row in reader:
                    url, username, password, totp, extra, name, grouping, fav = row
                    try:
                        cursor.execute('''
                        INSERT OR IGNORE INTO passwords (url, username, password, totp, extra, name, grouping, fav)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                        ''', (url, username, password, totp, extra, name, grouping, fav))
                        print("[ ✓ ] Inserted record.")
                    except sqlite3.IntegrityError:print("[ ✕ ] Record not inserted.")

        conn.commit()
        conn.close()
        
    def modify():
        
        conn = sqlite3.connect('/usr/local/etc/me/local/share/database/password.db')
        cursor = conn.cursor()

        search_value = input('Enter a search value: ')
        
        cursor.execute(
            'SELECT url, username, password, name FROM passwords WHERE url LIKE ? OR username LIKE ?',
            ('%' + search_value + '%', '%' + search_value + '%')
        )

        results = cursor.fetchall()
        for i, row in enumerate(results):
        
            print(f"""\n
{i} - URL: {Passwd.short_url(row[0])}
- Name: {row[3]}
- Username: {row[1]}""")

        result_number = int(input('[0] Enter the number of a result to display: '))

        selected_row = results[result_number - 1]
        
        cursor.execute(
            'DELETE FROM passwords WHERE url = ? AND username = ? AND name = ?',
            (selected_row[0], selected_row[1], selected_row[3])
        )
        
        conn.commit()
        cursor.close()
        conn.close()
        
    def add():
        
        conn = sqlite3.connect('/usr/local/etc/me/local/share/database/password.db' )
        cursor = conn.cursor()

        url = input('Enter the URL: ')
        username = input('Enter the username: ')
        password = input('Enter the password: ')
        name = input('Enter the name: ')

        cursor.execute(
            'INSERT INTO passwords (url, username, password, name) VALUES (?, ?, ?, ?)',
            (url, username, password, name)
        )

        conn.commit()
        cursor.close()
        conn.close()
    
    def copy():
        
        conn = sqlite3.connect('/usr/local/etc/me/local/share/database/password.db')
        cursor = conn.cursor()

        search_value = input('Enter a search value: ')
        
        cursor.execute(
            'SELECT url, username, password, name FROM passwords WHERE url LIKE ? OR username LIKE ?',
            ('%' + search_value + '%', '%' + search_value + '%')
        )

        results = cursor.fetchall()
        for i, row in enumerate(results):
        
            print(f"""\n
{i} - URL: {Passwd.short_url(row[0])}
- Name: {row[3]}
- Username: {row[1]}""")

        result_number = int(input('[0] Enter the number of a result to display: '))

        selected_row = results[result_number - 1]
        print(f"""URL: {Passwd.short_url(row[0])} >> Copied to clipboard""")
        clipboard.copy(selected_row[2])

        conn.close()

    def short_url(url):
        parsed_url = urlparse(url)
        domain = parsed_url.netloc    
        return domain
    
class GeneratePasswd:
    
    def new():
        
        lists = "abcdefghijklmnñopqrstuvwxyzºª!|·#$%&¬/()=?¿¡.:-_,;*{,}ç^[+]0123456789ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        length = input("[12] (minimum 8) Length: ")
        if length == '': length = 12
        while length <= 8:
            length = input("[12] (minimum 8) Length: ")
        password = ""
        for x in range(length):
            a = random.choice(str(lists))
            password += a
        
        print(password)
