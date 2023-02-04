# me

# DO NOT CLONE OR RUN THE SCRIPT, IT IS UNDER DEVELOPMENT AND MAY GENERATE PROBLEMS ON YOUR PC

# NO CLONE NI EJECUTE EL SCRIPT, ESTA BAJO DESARROLLO Y PUEDE GENERAR PROBLEMAS EN SU PC

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
