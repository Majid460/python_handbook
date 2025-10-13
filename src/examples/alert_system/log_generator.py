
import os
from dataclasses import dataclass
from datetime import datetime

filename = "app.log"

def check_file_exist():
    if not os.path.exists(filename):
        print(f"{filename} not found. Creating new log file...")
        with open(filename,'w') as f:
            f.write("=== Log File Created ===\n")

def write_logs(level,message):
    check_file_exist()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(filename,'a') as f:
        f.write(f"{timestamp} - [{level}] {message}\n")


# Write message
@dataclass
class Log:
    level : str
    message : str
lis_message = [Log("INFO","User login successful"),Log("INFO","Request latency=312ms"),Log("ERROR","Payment service unavailable"),Log("FAILURE","Disk read timeout"),Log("INFO","User logout successful")]

[write_logs(i.level,i.message) for i in lis_message]
print("Log file created")

