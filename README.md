# me

Me is an application that allows you to perform certain basic tasks. Manage passwords, contacts, tasks, notes, search the web with a command, emulate python, among others!

Me is an application that allows you to perform certain tasks from the terminal, review the [Avilable Commands](https://github.com/14wual/me#avilable-commands) to discover all its features!

```
                Welcome to Me! 
▒█▀▄▀█ ▒█▀▀▀    User: {self.config.get("me", "user")}
▒█▒█▒█ ▒█▀▀▀    Version: V.{self.config.get("me", "version")} 
▒█░░▒█ ▒█▄▄▄    Now: {MeAPP.formatted_time}
                (code by wual)
```

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
1. [Usage](https://github.com/14wual/me#usage)
2. [Avilable Commands](https://github.com/14wual/me#avilable-commands)
3. [Install](https://github.com/14wual/me#install)
4. [Gallery](https://github.com/14wual/me#install)
5. [Possible Mistakes](https://github.com/14wual/me#possible-mistakes)
   4.1 [Command does not exist](https://github.com/14wual/me#command-does-not-exist)
   4.2 [NoSectionError](https://github.com/14wual/me#nosectionerror)
6. About
   5.1 [License](https://github.com/14wual/me#license)
   5.2 [Know Me](https://github.com/14wual/me#-know-me)

## Usage

**There are two ways to use /me**

1. From your own terminal: **`me avilable-command argument`** | Example **`me password --modify`**
2. From the terminal /me:  **`avilable-command argument opcional-argument`** | Example: **`contacts --search Wual`**

Type `help` in the terminal me or `me help` in your own terminal to see all available commands.

## Avilable Commands:

```
Browser Commands:
    browser: search and browse bookmarks.
    browser --add/-a: add a new bookmark.
    browser --delete/-d: delete a new bookmark.
    browser --list/-l: list your bookmarks.
    search: do a google search.
    
    *Shortcuts: [search], [browser], [b], [s], [brow]

[mail]: Send an email.
    
[contacts] Contacts Commands:
    contacts --modify/-m: look for a contact.
    contacts --search/-s: modify an existing contact.
    contacts --add/-a: add a new contact.
    contacts --delete/-d: delete an existing contact.
    
    *Shortcuts: [contacts], [cont], [c]

[passwd] Password Commands:
    passwd --add/-a: Add New Key to Vault.
    passwd --copy/-c: Search & Copy Key from Vault.
    passwd --matter: Import Keys from csv to Vault.
    passwd --modify/-m: Search & Modify Key from Vault.
    
    *Shortcuts: [password], [passwd], [p]

[task] Tasks Commands:
    task --add/-a: Add New Task.
    task --done/-d: Mark a task as done.
    task --list/-l: List all pending tasks
    task --today/-t: Read today's tasks.

    *Shortcuts: [task], [t]
    
[notes] Notes Commands:
    notes --new/-n: Create a new note.
    notes --read/-r: View all notes, select one write/read.
    notes --delete/-d: Delete a note.
    
    *Shortcuts: [notes], [n]
    
[pc] PC Commands:
    pc --all/-a: Print all logs
    pc --ram/-r: Current status of: ram
    pc --cpu/-c: Current status of: cpu
    pc --disks/-d: Current status of: disks
    pc --processor/-p: Current status of: processor

[check] Check Commands:
    check --connect/-c: Check connectivity with a web or ip.
    check --path/-p: Check if a directory exists.
    check --file/-f: Ceck if a file exists.
    second options/optional: -w: write the directory, url, ... (string)
        check --command -w example
        
[python] or [py]: Create a python terminal.
    
Other Commands:
    [help] or [h]: display this panel
    clear/cls: clear terminal
    info/i: View app information
    hello/hi: Initial greeting of the app
    exit/bye: Exit the program
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
alias me='sudo python3 /usr/local/etc/me/pip/app/me/me/__init__.py'
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
mail = <your-mail@gmail.com>

[databases]
password = /usr/local/etc/me/local/share/database/password.db
browser = /usr/local/etc/me/usr/browser/log/favorites.csv
notes = /usr/local/etc/me/usr/txt/log/notes_inputs.csv
```

### Why does it ask me for sudo?

Due to the path where the program is located (it is in a common path in all operating systems and is there to create the fewest possible incompatibilities) it is necessary to ask for root. Since many of the functionalities write files inside the subpaths. Path `/usr/local/etc/me/`

## License
Copyright © 2023 Carlos Padilla.

This project is [MIT](https://github.com/14wual/me/blob/main/LICENSE) licensed.

## 🚀 Know me
Linkeding - https://www.linkedin.com/in/cpadilla10/ 

Twitter - https://twitter.com/codewual 

YouTube - https://www.youtube.com/channel/UC0B3mTwPPdKPEwLerauEtdg
