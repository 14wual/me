
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
