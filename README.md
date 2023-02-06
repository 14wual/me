# me

Me is an application that allows you to perform certain tasks from the terminal, from having your own (simple) password manager, searching from the web, managing hyperlinks (that is, shortcuts), notes, tasks, ...

```
888       888 888     888       d8888 888
888   o   888 888     888      d88888 888
888  d8b  888 888     888     d88P888 888        (code by WUAL)
888 d888b 888 888     888    d88P 888 888            twitter.com/codewual
888d88888b888 888     888   d88P  888 888     github.com/14wual
88888P Y88888 888     888  d88P   888 888            youtube: WualPK
8888P   Y8888 Y88b. .d88P d8888888888 888     
888P     Y888  "Y88888P" d88P     888 88888888
```

1. [Avilable Commands](https://github.com/14wual/me#avilable-commands)
2. [Install](https://github.com/14wual/me#install)
3. [Gallery](https://github.com/14wual/me#install)
4. [Possible Mistakes](https://github.com/14wual/me#possible-mistakes)
   4.1 [Command does not exist](https://github.com/14wual/me#command-does-not-exist)
   4.2 [NoSectionError](https://github.com/14wual/me#nosectionerror)
5. About
   5.1 [License](https://github.com/14wual/me#license)
   5.2 [Know Me](https://github.com/14wual/me#-know-me)

## Avilable Commands:

```
Browser Commands: 
     browser: search and browse bookmarks. 
     browser --add: add a new bookmark. 
     browser --delete: delete a new bookmark. 
     browser --list: list your bookmarks. 
     search: do a google search. 
      
[contacts] Contacts Commands: 
     contacts --modify: look for a contact. 
     contacts --search: modify an existing contact. 
     contacts --add: add a new contact. 
     contacts --delete: delete an existing contact. 
  
[passwd] | Password Commands: 
     passwd --add: Add New Key to Vault 
     passwd --copy: Search & Copy Key from Vault 
     passwd --matter: Import Keys from csv to Vault 
     passwd --modify: Search & Modify Key from Vault 
      
[notes] Notes Commands: 
     notes --new: Create a new note 
     notes --read: View all notes, select one write/read 
     notes --delete: Delete a note 
      
Other Commands: 
     clear/cls: clear terminal 
     info: View app information 
     mypc: View current hardware/software status 
     hello/hi: Initial greeting of the app 
     exit/bye: Exit the program""")
```

## Install

### Follow the steps below carefully

Clone the repository and go into the me/ folder

```bash
git clone https://github.com/14wual/me.git
cd me
```

Give the bash setup file execution permission

```bash
sudo chmod +x install.sh
```

Run the file 'install-sh' >> `./install.sh`

```bash
./install.sh
```

Log out and log in again (`kill -9 -1`)

## Gallery

![14wual/Me - BV0.63](https://user-images.githubusercontent.com/105047274/216813795-52684672-216b-430d-9b6a-b3456f44c981.png)


## Possible mistakes

### Command does not exist

Modify your rc file, either `.bashrc` or `.zshrc`

```
nano .zshrc
```

```bash
# Go to the last row and write the following
alias me='python3 /home/<your-user>/.config/me/pip/app/me/me/__init__.py'
```

### NoSectionError

Modify the content of the following file: `/home/example/.config/me/bin/me/me.ini`, changing the data for your information.
Don't forget to modify the paths.

File content:

```ini
[me]
version = 0.1 
user = <your-user> 
password = <your-password>

[software]
browser = default

[databases]
password = /home/<your-user>/.config/me/local/share/database/password.db
browser = /home/<your-user>/.config/me/usr/browser/log/favorites.csv
notes = /home/<your-user>/.config/me/usr/txt/log/notes_inputs.csv
```

## License
Copyright © 2023 Carlos Padilla.

This project is [MIT](https://github.com/14wual/me/blob/main/LICENSE) licensed.

## 🚀 Know me
Linkeding - https://www.linkedin.com/in/cpadilla10/ 

Twitter - https://twitter.com/codewual 

YouTube - https://www.youtube.com/channel/UC0B3mTwPPdKPEwLerauEtdg
