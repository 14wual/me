# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# See proyect >> https://github.com/14wual/me
# Follow me >> https://twitter.com/codewual

# --------------------Extern Imports--------------------
import os
import socket

# --------------------Extern Imports--------------------
class Check:
    
    def connect(host):
    
        port = 80

        try:
            socket.create_connection((host, port), timeout=2)
            print(f"Connectivity established with {host}")
        except socket.error as e:print("Could not establish connection.")

        
    def path(path):
        
        try:
            os.path.exists(path)
            print(f"Path '{path}' exists.")
            files = 0
            directories = 0
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                if os.path.isdir(item_path):directories += 1
                else:files += 1

            print("Files:", files)
            print("Directories:", directories)

        except:print(f"Path '{path}' does not exist.")
        
                    
    def files(file_path):
        
        if os.path.isfile(file_path):print(f"File '{file_path}' exists.")
        else:print(f"File '{file_path}' does not exist.")
