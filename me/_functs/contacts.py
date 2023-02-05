# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# See proyect >> https://github.com/14wual/me
# Follow me >> https://twitter.com/codewual

# --------------------Extern Imports--------------------
import sqlite3
import os
        
# --------------------APP--------------------
class Search:

    def search_contact(value):
        
        ddbb_file_path = '/home/%s/.config/me/local/share/database/contacts.db' % os.environ['USER']
        conn = sqlite3.connect(ddbb_file_path)
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM contacts WHERE 
        name LIKE ? OR 
        surname LIKE ? OR 
        nickname LIKE ? OR 
        phone LIKE ? OR 
        mail LIKE ? OR 
        company LIKE ? OR 
        old_companies LIKE ? OR 
        web LIKE ? OR 
        tags LIKE ? OR 
        other LIKE ?
        """, ('%' + value + '%',) * 10)

        results = cursor.fetchall()

        if results:
            print("The following results were found:")
            contacts_id = []
            for i, result in enumerate(results):
                contacts_id.append(result[0])
                print(f"{i+1}. Name: {result[1]} {result[2]}")
                print("Has worked on", result[6], result[7])
                
            while True:
                user_choice = input("Select a number to view contact details: ")
                try:
                    user_choice = int(user_choice)
                    if user_choice in range(1, len(contacts_id) + 1):
                        selected_contact_id = contacts_id[user_choice - 1]
                        break
                    else:print("Invalid option. Try again.")
                except ValueError:print("Invalid option. Try again.")
 
            cursor.execute(f"SELECT * FROM contacts WHERE id={selected_contact_id}")
            selected_contact = cursor.fetchone()

            print("\nContact details:")
            print("ID:", selected_contact[0])
            print("Name:", selected_contact[1])
            print("Surname:", selected_contact[2])
            print("Nickname:", selected_contact[3])
            print("Phone:", selected_contact[4])
            print("Email:", selected_contact[5])
            print("Company:", selected_contact[6])
            print("Past Companies:", selected_contact[7])
            print("Website:", selected_contact[8])
            print("Tags:", selected_contact[9])
            print("Other:", selected_contact[10])

        else:print("No results found.")
        conn.close()
        
class Add:
    
    def contact_info():
        
        print("New Contact > ")
        name = input("[*] name: ")
        surname = input("[*] surname: ")
        nickname = input("[] nickname: ")
        phone = input("[] phone: ")
        email = input("[] email: ")
        company = input("[] company: ")
        past_companies = input("[] past_companies: ")
        website = input("[] website: ")
        tags  = input("[] tags : ")
        other = input("[] other: ")
        print("\n")
        
        Add.add_contact(
            name=name, surname=surname, nickname=nickname, phone=phone, 
            email=email, company=company, past_companies=past_companies, 
            website=website, tags=tags, other=other)
    
    def add_contact(name, surname, nickname, phone, email, company, past_companies, website, tags, other):
        ddbb_file_path = '/home/%s/.config/me/local/share/database/contacts.db' % os.environ['USER']
        conn = sqlite3.connect(ddbb_file_path)
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO contacts (name, surname, nickname, phone, mail, company, old_companies, web, tags, other)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (name, surname, nickname, phone, email, company, past_companies, website, tags, other))

        conn.commit()
        print("Contact added successfully.")
        conn.close()
        
class Modify:
    
    def delete_contact(value):
        ddbb_file_path = '/home/%s/.config/me/local/share/database/contacts.db' % os.environ['USER']
        conn = sqlite3.connect(ddbb_file_path)
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM contacts WHERE 
        name LIKE ? OR 
        surname LIKE ? OR 
        nickname LIKE ? OR 
        phone LIKE ? OR 
        mail LIKE ? OR 
        company LIKE ? OR 
        old_companies LIKE ? OR 
        web LIKE ? OR 
        tags LIKE ? OR 
        other LIKE ?
        """, ('%' + value + '%',) * 10)

        results = cursor.fetchall()

        if results:
            print("The following results were found:")
            contacts_id = []
            for i, result in enumerate(results):
                contacts_id.append(result[0])
                print(f"{i+1}. Name: {result[1]} {result[2]}")
                print("Has worked on", result[6], result[7])
                
            while True:
                user_choice = input("Select a number to view contact details: ")
                try:
                    user_choice = int(user_choice)
                    if user_choice in range(1, len(contacts_id) + 1):
                        selected_contact_id = contacts_id[user_choice - 1]
                        break
                    else:print("Invalid option. Try again.")
                except ValueError:print("Invalid option. Try again.")
 
            cursor.execute(f"DELETE FROM contacts WHERE id={selected_contact_id}")
            conn.commit()
            
            print("Contact deleted.")
            conn.close()
            
        else:print("No results found.")
    
    def modify_contact(value):
        ddbb_file_path = '/home/%s/.config/me/local/share/database/contacts.db' % os.environ['USER']
        conn = sqlite3.connect(ddbb_file_path)
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM contacts WHERE 
        name LIKE ? OR 
        surname LIKE ? OR 
        nickname LIKE ? OR 
        phone LIKE ? OR 
        mail LIKE ? OR 
        company LIKE ? OR 
        old_companies LIKE ? OR 
        web LIKE ? OR 
        tags LIKE ? OR 
        other LIKE ?
        """, ('%' + value + '%',) * 10)

        results = cursor.fetchall()

        if results:
            print("The following results were found:")
            contacts_id = []
            for i, result in enumerate(results):
                contacts_id.append(result[0])
                print(f"{i+1}. Name: {result[1]} {result[2]}")
                print("Has worked on", result[6], result[7])
                
            while True:
                user_choice = input("Select a number to view contact details: ")
                try:
                    user_choice = int(user_choice)
                    if user_choice in range(1, len(contacts_id) + 1):
                        selected_contact_id = contacts_id[user_choice - 1]
                        break
                    else:print("Invalid option. Try again.")
                except ValueError:print("Invalid option. Try again.")
        
            cursor.execute(f"SELECT * FROM contacts WHERE id={selected_contact_id}")
            selected_contact = cursor.fetchone()
            
            new_name = input(f"[{selected_contact[1]}] Write a new name: ")
            if new_name == "":new_name= selected_contact[1]
            new_surname = input(f"[{selected_contact[2]}] Write a new surname: ")
            if new_surname == "":new_surname= selected_contact[2]
            new_nickname = input(f"[{selected_contact[3]}] Write a new nickname: ")
            if new_nickname == "":new_nickname= selected_contact[3]
            new_phone = input(f"[{selected_contact[4]}] Write a new phone: ")
            if new_phone == "":new_phone= selected_contact[4]
            new_mail = input(f"[{selected_contact[5]}] Write a new mail: ")
            if new_mail == "":new_mail= selected_contact[5]
            new_company = input(f"[{selected_contact[6]}] Write a new company: ")
            if new_company == "":new_company= selected_contact[6]
            new_old_companies = input(f"[{selected_contact[7]}] Write a new old companies: ")
            if new_old_companies == "":new_old_companies= selected_contact[7]
            new_web = input(f"[{selected_contact[8]}] Write a new web: ")
            if new_web == "":new_web= selected_contact[8]
            new_tags = input(f"[{selected_contact[9]}] Write a new tags: ")
            if new_tags == "":new_tags= selected_contact[9]
            new_other= input(f"[{selected_contact[10]}] Write a new other: ")
            if new_other == "":new_other= selected_contact[10]
            
            print(f"""
Details:
    New name: {new_name}
    New surname: {new_surname}
    New nickname: {new_nickname}
    New phone: {new_phone}
    New mail: {new_mail}
    New company: {new_company}
    New old_companies: {new_old_companies}
    New web: {new_web}
    New tags: {new_tags}
    New other: {new_other}""")
            
            confirm = input("[Y/n] The information is correct?")
            if confirm == "": confirm = "Y"
            if confirm == "Y" or confirm == "y":
                cursor.execute(f"UPDATE contacts SET name='{new_name}', surname='{new_surname}', nickname='{new_nickname}', phone='{new_phone}', mail='{new_mail}', company='{new_company}', old_companies='{new_old_companies}', web='{new_web}', tags='{new_tags}', other='{new_other}' WHERE id={selected_contact_id}")
                print("Modified contact.")
                conn.commit()
                
        else:
            print("No results found.")
