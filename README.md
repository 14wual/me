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

Modify your rc file, either `.bashrc` or `.zshrc`

```
nano .zshrc
```

```bash
# Go to the last row and write the following
alias me='python3 /home/<your-user>/.config/me/pip/app/me/me/__init__.py'
```

Log out and log in again (`kill -9 -1`)
