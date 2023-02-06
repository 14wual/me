# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# See proyect >> https://github.com/14wual/me
# Follow me >> https://twitter.com/codewual

# --------------------Extern Imports--------------------
try:import psutil
except ImportError: raise ImportError("Failed to import psutil. Make sure it is installed correctly and is in the PYTHONPATH.")

# --------------------APP--------------------
class PC:
    
    def cpu():
                
        print(f"""
CPU Logical Count: {psutil.cpu_count()},
CPU Fisical Count: {psutil.cpu_count(logical=False)},
CPU Percent: {psutil.cpu_percent()},
CPU Freq: {psutil.cpu_freq()},
              """)
        
    def memory():
        
        print(f"""
Avilable: {psutil.virtual_memory().available}MB,
Percent: {psutil.virtual_memory().percent}%,
Free: {psutil.virtual_memory().free}MB,
              """)
    def processes():
        
        i=0
        list_processes = []
        for proc in psutil.process_iter():i+=1;list_processes.append(proc)
        
        print(f"Total processes: {i}")
        
        confirm = input("[N/y] See processes")
        if confirm == "":confirm='n'
        
        if confirm == 'y' or confirm == 'Y':
            for i, proc in enumerate(psutil.process_iter()):
                print(proc)
                if (i % 15 == 0):
                    continues = input("Press to continue... or Write 'exit': ")
                    if continues == 'exit':break
                       
    def disk():
        
        disk_info = psutil.disk_usage('/')
        
        print(f"""
Main total: {disk_info.total}MB,
Main used: {disk_info.used}MB,
Main free: {disk_info.free}MB,
              """)
