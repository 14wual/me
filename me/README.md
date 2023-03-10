Do not try to install the repository with dpkg or using the .deb file. This is still under development and is in an unstable version

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
6. About
   5.1 [License](https://github.com/14wual/me#license)
   5.2 [Know Me](https://github.com/14wual/me#-know-me)

## Usage

**There are two ways to use /me**

1. From your own terminal: **`me avilable-command argument`** | Example **`me password --modify`**
2. From the terminal /me:  **`avilable-command argument opcional-argument`** | Example: **`contacts --search Wual`**

Type `help` in the terminal me or `me help` in your own terminal to see all available commands.

## Avilable Commands:

### Browser

```
Browser Commands:
    browser: search and browse bookmarks.
    browser --add/-a: add a new bookmark.
    browser --delete/-d: delete a new bookmark.
    browser --list/-l: list your bookmarks.
    search: do a google search.
    
    *Shortcuts: [search], [browser], [b], [s], [brow]
```

### Mail

```
[mail]: Send an email.
```
### Contact book

```
[contacts] Contacts Commands:
    contacts --modify/-m: look for a contact.
    contacts --search/-s: modify an existing contact.
    contacts --add/-a: add a new contact.
    contacts --delete/-d: delete an existing contact.
    
    *Shortcuts: [contacts], [cont], [c]
```

### Password manager

```
[passwd] Password Commands:
    passwd --add/-a: Add New Key to Vault.
    passwd --copy/-c: Search & Copy Key from Vault.
    passwd --matter: Import Keys from csv to Vault.
    passwd --modify/-m: Search & Modify Key from Vault.
    passwd --generate/-gen/-g: Generate a new password.
    
    *Shortcuts: [password], [passwd], [p]
```

### Task Manager

```
[task] Tasks Commands:
    task --add/-a: Add New Task.
    task --done/-d: Mark a task as done.
    task --list/-l: List all pending tasks
    task --today/-t: Read today's tasks.

    *Shortcuts: [task], [t]
```

### Notes app

```
[notes] Notes Commands:
    notes --new/-n: Create a new note.
    notes --read/-r: View all notes, select one write/read.
    notes --delete/-d: Delete a note.
    
    *Shortcuts: [notes], [n]
```

### Performance commands

```    
[pc] PC Commands:
    pc --all/-a: Print all logs
    pc --ram/-r: Current status of: ram
    pc --cpu/-c: Current status of: cpu
    pc --disks/-d: Current status of: disks
    pc --processor/-p: Current status of: processor
```

### File Manager

```
File manager:
    SAVE:
        save --save/-s: save the path where you are. (max 3)
        save --view/-v: view saved paths.
    ls: shows all files and folders contained in a specific folder.
    ls -a: shows all files and folders (including hidden ones) contained in a specific folder.
    cd: change directory.
    pwd: view current path.   
    cp: Copy and paste files: allows you to copy files from one folder to another.
    mv: allows you to move files from one folder to another.
    rm: Delete Files:  Allows the user to delete unnecessary or unwanted files.
    rm -r:Delete Directories:  Allows the user to delete unnecessary or unwanted directories.
    mkdir: Create Folders: Allows the user to create new folders to organize their files.
    view: View File Details: Displays detailed information about a file, such as its size, creation date, and file type.
    ren: Rename Files: Allows the user to rename a file to make it easier to find

```

### Checks

```
[check] Check Commands:
    check --connect/-c: Check connectivity with a web or ip.
    check --path/-p: Check if a directory exists.
    check --file/-f: Ceck if a file exists.
    second options/optional: -w: write the directory, url, ... (string)
        check --command -w example
```

### Games

```
- To find out more, run the command [games]
- To play a game run the following commands: [rps] [gtn] [mga]

1. [RPS] Rock, Paper, Scissors:
    It consists of three options: rock, paper or scissors. Each player chooses an option, and then they are compared 
    to determine who wins. Rock beats scissors, scissors beats paper, and paper beats rock. In the event of a tie, the
    game is played again until someone wins.
2. [GTN] Guess the number:
    This game consists of the program choosing a random number and the user has to guess it. Each time the user makes 
    a guess, the program tells the user if the number is larger or smaller until the user guesses the correct number.
```

### Terminal Python

Under development

```     
[python] or [py]: Create a python terminal.
```

### Other /me commands

```
Other Commands:
    [help] or [h]: display this panel
    clear/cls: clear terminal
    info/i: View app information
    hello/hi: Initial greeting of the app
    exit/bye: Exit the program
```

<details>

<summary>Show Set</summary>

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
    passwd --generate/-gen/-g: Generate a new password.
    
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
    pc --ram/-r: Current status of: do
    pc --cpu/-c: Current status of: cpu
    pc --disks/-d: Current status of: disks
    pc --processor/-p: Current status of: processor

[check] Check Commands:
    check --connect/-c: Check connectivity with a web or ip.
    check --path/-p: Check if a directory exists.
    check --file/-f: Ceck if a file exists.
    second options/optional: -w: write the directory, url, ... (string)
        check --command -w example
        
File manager:
    SAVE:
        save --save/-s: save the path where you are. (max 3)
        save --view/-v: view saved paths.
    ls: shows all files and folders contained in a specific folder.
    ls -a: shows all files and folders (including hidden ones) contained in a specific folder.
    cd: change directory.
    pwd: view current path.
    cp: Copy and paste files: allows you to copy files from one folder to another.
    mv: allows you to move files from one folder to another.
    rm: Delete Files:  Allows the user to delete unnecessary or unwanted files.
    rm -r:Delete Directories:  Allows the user to delete unnecessary or unwanted directories.
    mkdir: Create Folders: Allows the user to create new folders to organize their files.
    view: View File Details: Displays detailed information about a file, such as its size, creation date, and file type.
    ren: Rename Files: Allows the user to rename a file to make it easier to find

[python] or [py]: Create a python terminal.

GAMES:
 - To play a game run the following commands: [rps] [gtn] [mga]
 - To find out more, run the command [games]
    
Other Commands:
    [help] or [h]: display this panel
    clear/cls: clear terminal
    info/i: View app information
    hello/hi: Initial greeting of the app
    exit/bye: Exit the program
```

</details>

## Install

### Follow the steps below carefully

Clone the repository and go into the me/ folder

```bash
git clone https://github.com/14wual/me.git
cd me/me/_install
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

### Error: argument

On different occasions we write the arguments requested by the commands correctly, but an error something similar to this does not appear: `usage: __init__.py [-example0] [-example1]` and `__init__.py: error: argument '-example_argument': expected 1 argument`
This is because of the way the `argparse` library is created, if this error still occurs, type the command with the argument and then a "random" text after | Example: `password --generate skdxpmpmd`

## Fun facts

### Autocomplete

Did you know that /me has an **autocompletion**, this is used for the arguments of the different commands | Example, type '`contacts --m`' and press `tab` and you will see that '`--m`' becomes '`--modify`'

## License
Copyright © 2023 Carlos Padilla.

This project is [MIT](https://github.com/14wual/me/blob/main/LICENSE) licensed.

## 🚀 Know me
Linkeding - https://www.linkedin.com/in/cpadilla10/ 

Twitter - https://twitter.com/codewual 

YouTube - https://www.youtube.com/channel/UC0B3mTwPPdKPEwLerauEtdg
